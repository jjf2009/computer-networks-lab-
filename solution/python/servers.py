#!/usr/bin/env python3
"""Small teaching implementations of chat, HTTP, and FTP servers.

Run: python3 servers.py chat|web|ftp [options]
These are intentionally simple and suitable for localhost/LAN lab testing.
"""
from __future__ import annotations
import argparse, mimetypes, os, socket, threading
from pathlib import Path

BUF = 4096

def chat_server(host: str, port: int) -> None:
    clients: set[socket.socket] = set(); lock = threading.Lock()
    def client(conn: socket.socket, addr):
        with conn:
            conn.sendall(b"Welcome. Type messages; /quit exits.\n")
            with lock: clients.add(conn)
            try:
                while True:
                    data = conn.recv(BUF)
                    if not data or data.strip() == b"/quit": break
                    msg = f"[{addr[0]}:{addr[1]}] ".encode() + data
                    with lock:
                        for peer in list(clients):
                            if peer is not conn:
                                try: peer.sendall(msg)
                                except OSError: clients.discard(peer)
            finally:
                with lock: clients.discard(conn)
    with socket.socket() as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1); s.bind((host, port)); s.listen()
        print(f"chat listening on {host}:{port}")
        while True:
            conn, addr = s.accept(); threading.Thread(target=client, args=(conn, addr), daemon=True).start()

def web_server(host: str, port: int, root: Path) -> None:
    root = root.resolve()
    def client(conn: socket.socket, addr):
        with conn:
            request = conn.recv(BUF).decode("iso-8859-1", "replace")
            line = request.splitlines()[0] if request else ""
            parts = line.split()
            if len(parts) < 2 or parts[0] != "GET":
                body = b"HTTP/1.1 400 Bad Request\r\n\r\n"; conn.sendall(body); return
            rel = parts[1].split("?", 1)[0].lstrip("/") or "index.html"
            path = (root / rel).resolve()
            if root not in path.parents and path != root or not path.is_file():
                body = b"<h1>404 Not Found</h1>"; head = b"HTTP/1.1 404 Not Found"
            else:
                body = path.read_bytes(); head = b"HTTP/1.1 200 OK"
            typ = mimetypes.guess_type(str(path))[0] or "application/octet-stream"
            conn.sendall(head + f"\r\nContent-Length: {len(body)}\r\nContent-Type: {typ}\r\nConnection: close\r\n\r\n".encode() + body)
    with socket.socket() as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1); s.bind((host, port)); s.listen()
        print(f"web listening on http://{host}:{port}, root={root}")
        while True:
            conn, addr = s.accept(); threading.Thread(target=client, args=(conn, addr), daemon=True).start()

def ftp_server(host: str, port: int, root: Path) -> None:
    root = root.resolve()
    def safe(name):
        p = (root / name.lstrip("/" if name else "")).resolve()
        return p if root in p.parents or p == root else None
    def client(conn, addr):
        with conn:
            cwd = Path("."); conn.sendall(b"220 SimpleLab FTP ready\r\n")
            def reply(x): conn.sendall((x + "\r\n").encode())
            while True:
                raw = conn.recv(BUF)
                if not raw: break
                cmd, _, arg = raw.decode("utf-8", "replace").strip().partition(" "); cmd = cmd.upper()
                if cmd == "USER": reply("331 Password required")
                elif cmd == "PASS": reply("230 Logged in (lab mode)")
                elif cmd == "SYST": reply("215 UNIX Type: L8")
                elif cmd == "PWD": reply(f'257 "/{cwd}"')
                elif cmd == "CWD":
                    p = safe(str(cwd / arg))
                    if p and p.is_dir(): cwd = p.relative_to(root); reply("250 Directory changed")
                    else: reply("550 No such directory")
                elif cmd == "LIST":
                    reply("150 Here comes the directory listing")
                    for p in sorted((root / cwd).iterdir()): conn.sendall((p.name + "\r\n").encode())
                    reply("226 Directory send OK")
                elif cmd == "RETR":
                    p = safe(str(cwd / arg))
                    if not p or not p.is_file(): reply("550 File unavailable"); continue
                    reply("150 Opening data (lab simplification)"); conn.sendall(p.read_bytes()); reply("226 Transfer complete")
                elif cmd == "QUIT": reply("221 Goodbye"); break
                else: reply("502 Command not implemented")
    with socket.socket() as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1); s.bind((host, port)); s.listen()
        print(f"ftp listening on {host}:{port}, root={root}")
        while True:
            conn, addr = s.accept(); threading.Thread(target=client, args=(conn, addr), daemon=True).start()

def main():
    ap = argparse.ArgumentParser(); sub = ap.add_subparsers(dest="kind", required=True)
    for kind, default in (("chat", 5000), ("web", 8080), ("ftp", 2121)):
        p = sub.add_parser(kind); p.add_argument("--host", default="0.0.0.0"); p.add_argument("--port", type=int, default=default); p.add_argument("--root", type=Path, default=Path("lab_root"))
    a = ap.parse_args(); a.root.mkdir(parents=True, exist_ok=True)
    {"chat": chat_server, "web": web_server, "ftp": ftp_server}[a.kind](a.host, a.port, a.root)
if __name__ == "__main__": main()
