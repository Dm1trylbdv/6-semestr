Last login: Sat Jun  3 03:08:59 on ttys007
lbdv@Air-Dmitrij ~ % brew install python3
sudo easy_install pip

Running `brew update --auto-update`...
==> Auto-updated Homebrew!
Updated 2 taps (homebrew/core and homebrew/cask).
==> New Formulae
ddns-go                    spotify_player             wzprof
git-credential-oauth       swift-outdated
libecpint                  tern
==> New Casks
loupedeck

You have 6 outdated formulae installed.

==> Fetching dependencies for python@3.11: mpdecimal, ca-certificates, openssl@1.1, readline and sqlite
==> Fetching mpdecimal
==> Downloading https://ghcr.io/v2/homebrew/core/mpdecimal/manifests/2.5.1
######################################################################### 100.0%
==> Downloading https://ghcr.io/v2/homebrew/core/mpdecimal/blobs/sha256:91f795d7
==> Downloading from https://pkg-containers.githubusercontent.com/ghcr1/blobs/sh
######################################################################### 100.0%
==> Fetching ca-certificates
==> Downloading https://ghcr.io/v2/homebrew/core/ca-certificates/manifests/2023-
######################################################################### 100.0%
==> Downloading https://ghcr.io/v2/homebrew/core/ca-certificates/blobs/sha256:f6
==> Downloading from https://pkg-containers.githubusercontent.com/ghcr1/blobs/sh
######################################################################### 100.0%
==> Fetching openssl@1.1
==> Downloading https://ghcr.io/v2/homebrew/core/openssl/1.1/manifests/1.1.1u
######################################################################### 100.0%
==> Downloading https://ghcr.io/v2/homebrew/core/openssl/1.1/blobs/sha256:f0a7ff
==> Downloading from https://pkg-containers.githubusercontent.com/ghcr1/blobs/sh
######################################################################### 100.0%
==> Fetching readline
==> Downloading https://ghcr.io/v2/homebrew/core/readline/manifests/8.2.1
######################################################################### 100.0%
==> Downloading https://ghcr.io/v2/homebrew/core/readline/blobs/sha256:abe9d3f3e
==> Downloading from https://pkg-containers.githubusercontent.com/ghcr1/blobs/sh
######################################################################### 100.0%
==> Fetching sqlite
==> Downloading https://ghcr.io/v2/homebrew/core/sqlite/manifests/3.42.0
######################################################################### 100.0%
==> Downloading https://ghcr.io/v2/homebrew/core/sqlite/blobs/sha256:4bbf2bd9382
==> Downloading from https://pkg-containers.githubusercontent.com/ghcr1/blobs/sh
######################################################################### 100.0%
==> Fetching python@3.11
==> Downloading https://ghcr.io/v2/homebrew/core/python/3.11/manifests/3.11.3
######################################################################### 100.0%
==> Downloading https://ghcr.io/v2/homebrew/core/python/3.11/blobs/sha256:598446
==> Downloading from https://pkg-containers.githubusercontent.com/ghcr1/blobs/sh
######################################################################### 100.0%
==> Installing dependencies for python@3.11: mpdecimal, ca-certificates, openssl@1.1, readline and sqlite
==> Installing python@3.11 dependency: mpdecimal
==> Pouring mpdecimal--2.5.1.ventura.bottle.tar.gz
🍺  /usr/local/Cellar/mpdecimal/2.5.1: 71 files, 2MB
==> Installing python@3.11 dependency: ca-certificates
==> Pouring ca-certificates--2023-05-30.ventura.bottle.tar.gz
cp: /private/tmp/d20230604-26670-14qkhv4/ca-certificates/.: unable to copy extended attributes to /usr/local/Cellar/ca-certificates/.: Bad file descriptor
cp: /usr/local/Cellar/ca-certificates/./2023-05-30: Permission denied
cp: /private/tmp/d20230604-26670-14qkhv4/ca-certificates/./2023-05-30: unable to copy extended attributes to /usr/local/Cellar/ca-certificates/./2023-05-30: Permission denied
cp: /usr/local/Cellar/ca-certificates/./2023-05-30/.brew: No such file or directory
cp: /private/tmp/d20230604-26670-14qkhv4/ca-certificates/./2023-05-30/.brew: unable to copy extended attributes to /usr/local/Cellar/ca-certificates/./2023-05-30/.brew: No such file or directory
cp: /usr/local/Cellar/ca-certificates/./2023-05-30/.brew/ca-certificates.rb: No such file or directory
cp: utimensat: /usr/local/Cellar/ca-certificates/./2023-05-30/.brew: No such file or directory
cp: chown: /usr/local/Cellar/ca-certificates/./2023-05-30/.brew: No such file or directory
cp: chmod: /usr/local/Cellar/ca-certificates/./2023-05-30/.brew: No such file or directory
cp: chflags: /usr/local/Cellar/ca-certificates/./2023-05-30/.brew: No such file or directory
cp: /private/tmp/d20230604-26670-14qkhv4/ca-certificates/./2023-05-30/.brew: unable to copy ACL to /usr/local/Cellar/ca-certificates/./2023-05-30/.brew: No such file or directory
cp: /usr/local/Cellar/ca-certificates/./2023-05-30/share: No such file or directory
cp: /private/tmp/d20230604-26670-14qkhv4/ca-certificates/./2023-05-30/share: unable to copy extended attributes to /usr/local/Cellar/ca-certificates/./2023-05-30/share: No such file or directory
cp: /usr/local/Cellar/ca-certificates/./2023-05-30/share/ca-certificates: No such file or directory
cp: /private/tmp/d20230604-26670-14qkhv4/ca-certificates/./2023-05-30/share/ca-certificates: unable to copy extended attributes to /usr/local/Cellar/ca-certificates/./2023-05-30/share/ca-certificates: No such file or directory
cp: /usr/local/Cellar/ca-certificates/./2023-05-30/share/ca-certificates/cacert.pem: No such file or directory
cp: utimensat: /usr/local/Cellar/ca-certificates/./2023-05-30/share/ca-certificates: No such file or directory
cp: chown: /usr/local/Cellar/ca-certificates/./2023-05-30/share/ca-certificates: No such file or directory
cp: chmod: /usr/local/Cellar/ca-certificates/./2023-05-30/share/ca-certificates: No such file or directory
cp: chflags: /usr/local/Cellar/ca-certificates/./2023-05-30/share/ca-certificates: No such file or directory
cp: /private/tmp/d20230604-26670-14qkhv4/ca-certificates/./2023-05-30/share/ca-certificates: unable to copy ACL to /usr/local/Cellar/ca-certificates/./2023-05-30/share/ca-certificates: No such file or directory
cp: utimensat: /usr/local/Cellar/ca-certificates/./2023-05-30/share: No such file or directory
cp: chown: /usr/local/Cellar/ca-certificates/./2023-05-30/share: No such file or directory
cp: chmod: /usr/local/Cellar/ca-certificates/./2023-05-30/share: No such file or directory
cp: chflags: /usr/local/Cellar/ca-certificates/./2023-05-30/share: No such file or directory
cp: /private/tmp/d20230604-26670-14qkhv4/ca-certificates/./2023-05-30/share: unable to copy ACL to /usr/local/Cellar/ca-certificates/./2023-05-30/share: No such file or directory
cp: utimensat: /usr/local/Cellar/ca-certificates/./2023-05-30: No such file or directory
cp: chown: /usr/local/Cellar/ca-certificates/./2023-05-30: No such file or directory
cp: chmod: /usr/local/Cellar/ca-certificates/./2023-05-30: No such file or directory
cp: chflags: /usr/local/Cellar/ca-certificates/./2023-05-30: No such file or directory
cp: /private/tmp/d20230604-26670-14qkhv4/ca-certificates/./2023-05-30: unable to copy ACL to /usr/local/Cellar/ca-certificates/./2023-05-30: Permission denied
cp: utimensat: /usr/local/Cellar/ca-certificates/.: Permission denied
cp: /private/tmp/d20230604-26670-14qkhv4/ca-certificates/.: unable to copy ACL to /usr/local/Cellar/ca-certificates/.: Bad file descriptor
Error: Failure while executing; `/usr/bin/env cp -pR /private/tmp/d20230604-26670-14qkhv4/ca-certificates/. /usr/local/Cellar/ca-certificates` exited with 1. Here's the output:
cp: /private/tmp/d20230604-26670-14qkhv4/ca-certificates/.: unable to copy extended attributes to /usr/local/Cellar/ca-certificates/.: Bad file descriptor
cp: /usr/local/Cellar/ca-certificates/./2023-05-30: Permission denied
cp: /private/tmp/d20230604-26670-14qkhv4/ca-certificates/./2023-05-30: unable to copy extended attributes to /usr/local/Cellar/ca-certificates/./2023-05-30: Permission denied
cp: /usr/local/Cellar/ca-certificates/./2023-05-30/.brew: No such file or directory
cp: /private/tmp/d20230604-26670-14qkhv4/ca-certificates/./2023-05-30/.brew: unable to copy extended attributes to /usr/local/Cellar/ca-certificates/./2023-05-30/.brew: No such file or directory
cp: /usr/local/Cellar/ca-certificates/./2023-05-30/.brew/ca-certificates.rb: No such file or directory
cp: utimensat: /usr/local/Cellar/ca-certificates/./2023-05-30/.brew: No such file or directory
cp: chown: /usr/local/Cellar/ca-certificates/./2023-05-30/.brew: No such file or directory
cp: chmod: /usr/local/Cellar/ca-certificates/./2023-05-30/.brew: No such file or directory
cp: chflags: /usr/local/Cellar/ca-certificates/./2023-05-30/.brew: No such file or directory
cp: /private/tmp/d20230604-26670-14qkhv4/ca-certificates/./2023-05-30/.brew: unable to copy ACL to /usr/local/Cellar/ca-certificates/./2023-05-30/.brew: No such file or directory
cp: /usr/local/Cellar/ca-certificates/./2023-05-30/share: No such file or directory
cp: /private/tmp/d20230604-26670-14qkhv4/ca-certificates/./2023-05-30/share: unable to copy extended attributes to /usr/local/Cellar/ca-certificates/./2023-05-30/share: No such file or directory
cp: /usr/local/Cellar/ca-certificates/./2023-05-30/share/ca-certificates: No such file or directory
cp: /private/tmp/d20230604-26670-14qkhv4/ca-certificates/./2023-05-30/share/ca-certificates: unable to copy extended attributes to /usr/local/Cellar/ca-certificates/./2023-05-30/share/ca-certificates: No such file or directory
cp: /usr/local/Cellar/ca-certificates/./2023-05-30/share/ca-certificates/cacert.pem: No such file or directory
cp: utimensat: /usr/local/Cellar/ca-certificates/./2023-05-30/share/ca-certificates: No such file or directory
cp: chown: /usr/local/Cellar/ca-certificates/./2023-05-30/share/ca-certificates: No such file or directory
cp: chmod: /usr/local/Cellar/ca-certificates/./2023-05-30/share/ca-certificates: No such file or directory
cp: chflags: /usr/local/Cellar/ca-certificates/./2023-05-30/share/ca-certificates: No such file or directory
cp: /private/tmp/d20230604-26670-14qkhv4/ca-certificates/./2023-05-30/share/ca-certificates: unable to copy ACL to /usr/local/Cellar/ca-certificates/./2023-05-30/share/ca-certificates: No such file or directory
cp: utimensat: /usr/local/Cellar/ca-certificates/./2023-05-30/share: No such file or directory
cp: chown: /usr/local/Cellar/ca-certificates/./2023-05-30/share: No such file or directory
cp: chmod: /usr/local/Cellar/ca-certificates/./2023-05-30/share: No such file or directory
cp: chflags: /usr/local/Cellar/ca-certificates/./2023-05-30/share: No such file or directory
cp: /private/tmp/d20230604-26670-14qkhv4/ca-certificates/./2023-05-30/share: unable to copy ACL to /usr/local/Cellar/ca-certificates/./2023-05-30/share: No such file or directory
cp: utimensat: /usr/local/Cellar/ca-certificates/./2023-05-30: No such file or directory
cp: chown: /usr/local/Cellar/ca-certificates/./2023-05-30: No such file or directory
cp: chmod: /usr/local/Cellar/ca-certificates/./2023-05-30: No such file or directory
cp: chflags: /usr/local/Cellar/ca-certificates/./2023-05-30: No such file or directory
cp: /private/tmp/d20230604-26670-14qkhv4/ca-certificates/./2023-05-30: unable to copy ACL to /usr/local/Cellar/ca-certificates/./2023-05-30: Permission denied
cp: utimensat: /usr/local/Cellar/ca-certificates/.: Permission denied
cp: /private/tmp/d20230604-26670-14qkhv4/ca-certificates/.: unable to copy ACL to /usr/local/Cellar/ca-certificates/.: Bad file descriptor

Password:
sudo: unable to execute /usr/local/bin/easy_install: No such file or directory
lbdv@Air-Dmitrij ~ % brew install python3
==> Fetching dependencies for python@3.11: ca-certificates, openssl@1.1, readline and sqlite
==> Fetching ca-certificates
==> Downloading https://ghcr.io/v2/homebrew/core/ca-certificates/manifests/2023-05-30
Already downloaded: /Users/lbdv/Library/Caches/Homebrew/downloads/09a7fdaf8b1e7b42a1d71bc93dbbf59c49cf6ca7a90f0968423b1bfef7d82f4c--ca-certificates-2023-05-30.bottle_manifest.json
==> Downloading https://ghcr.io/v2/homebrew/core/ca-certificates/blobs/sha256:f664c0f185677a82689ada2a4e
Already downloaded: /Users/lbdv/Library/Caches/Homebrew/downloads/8c6fc3fe81a7be60033c66d40a1b38563f1915ef2ff6ec7db569b7d8105da141--ca-certificates--2023-05-30.ventura.bottle.tar.gz
==> Fetching openssl@1.1
==> Downloading https://ghcr.io/v2/homebrew/core/openssl/1.1/manifests/1.1.1u
Already downloaded: /Users/lbdv/Library/Caches/Homebrew/downloads/7f1346f707232ded571b62177fa0dfcc5e02ee8bbc7fe4fc9883ca3f38acd2fe--openssl@1.1-1.1.1u.bottle_manifest.json
==> Downloading https://ghcr.io/v2/homebrew/core/openssl/1.1/blobs/sha256:f0a7ffd1772a1729d5f48d2e56b3a7
Already downloaded: /Users/lbdv/Library/Caches/Homebrew/downloads/5c9bacef185688e22aa57d140932696898b4f0d073504b6087a802d9773fef68--openssl@1.1--1.1.1u.ventura.bottle.tar.gz
==> Fetching readline
==> Downloading https://ghcr.io/v2/homebrew/core/readline/manifests/8.2.1
Already downloaded: /Users/lbdv/Library/Caches/Homebrew/downloads/ab483c9a913ae82f3a2b3ae20918791bc3bd6825c7122a29cd4f1e0c65413759--readline-8.2.1.bottle_manifest.json
==> Downloading https://ghcr.io/v2/homebrew/core/readline/blobs/sha256:abe9d3f3eec3ba2339860faa6a978b990
Already downloaded: /Users/lbdv/Library/Caches/Homebrew/downloads/02ffe281c52e32cbf982870b64e753dfd9527c5e0e5d81f0870e33bdead1fa27--readline--8.2.1.ventura.bottle.tar.gz
==> Fetching sqlite
==> Downloading https://ghcr.io/v2/homebrew/core/sqlite/manifests/3.42.0
Already downloaded: /Users/lbdv/Library/Caches/Homebrew/downloads/9054dbd2014cfa67115dbd42da881a047783b58c96344ba1d65317539985b631--sqlite-3.42.0.bottle_manifest.json
==> Downloading https://ghcr.io/v2/homebrew/core/sqlite/blobs/sha256:4bbf2bd9382c9f257712e60ff36fcddc7de
Already downloaded: /Users/lbdv/Library/Caches/Homebrew/downloads/1fa8e644ef7ceb1164689d924e0442526990d482bdc651ed6dfa9b1a5c786cf9--sqlite--3.42.0.ventura.bottle.tar.gz
==> Fetching python@3.11
==> Downloading https://ghcr.io/v2/homebrew/core/python/3.11/manifests/3.11.3
Already downloaded: /Users/lbdv/Library/Caches/Homebrew/downloads/6c839300228ac3383f7ebf7bcc20456ca127918286a03a9f3d41f00767e320d0--python@3.11-3.11.3.bottle_manifest.json
==> Downloading https://ghcr.io/v2/homebrew/core/python/3.11/blobs/sha256:59844694b2bb56614623c8ede16796
Already downloaded: /Users/lbdv/Library/Caches/Homebrew/downloads/f3fac6d805cf00191c9f9cc697a292e70db9b5c2e76c991ebd2dcda7de69306d--python@3.11--3.11.3.ventura.bottle.tar.gz
==> Installing dependencies for python@3.11: ca-certificates, openssl@1.1, readline and sqlite
==> Installing python@3.11 dependency: ca-certificates
==> Pouring ca-certificates--2023-05-30.ventura.bottle.tar.gz
cp: /private/tmp/d20230604-29041-desbuk/ca-certificates/.: unable to copy extended attributes to /usr/local/Cellar/ca-certificates/.: Bad file descriptor
cp: /usr/local/Cellar/ca-certificates/./2023-05-30: Permission denied
cp: /private/tmp/d20230604-29041-desbuk/ca-certificates/./2023-05-30: unable to copy extended attributes to /usr/local/Cellar/ca-certificates/./2023-05-30: Permission denied
cp: /usr/local/Cellar/ca-certificates/./2023-05-30/.brew: No such file or directory
cp: /private/tmp/d20230604-29041-desbuk/ca-certificates/./2023-05-30/.brew: unable to copy extended attributes to /usr/local/Cellar/ca-certificates/./2023-05-30/.brew: No such file or directory
cp: /usr/local/Cellar/ca-certificates/./2023-05-30/.brew/ca-certificates.rb: No such file or directory
cp: utimensat: /usr/local/Cellar/ca-certificates/./2023-05-30/.brew: No such file or directory
cp: chown: /usr/local/Cellar/ca-certificates/./2023-05-30/.brew: No such file or directory
cp: chmod: /usr/local/Cellar/ca-certificates/./2023-05-30/.brew: No such file or directory
cp: chflags: /usr/local/Cellar/ca-certificates/./2023-05-30/.brew: No such file or directory
cp: /private/tmp/d20230604-29041-desbuk/ca-certificates/./2023-05-30/.brew: unable to copy ACL to /usr/local/Cellar/ca-certificates/./2023-05-30/.brew: No such file or directory
cp: /usr/local/Cellar/ca-certificates/./2023-05-30/share: No such file or directory
cp: /private/tmp/d20230604-29041-desbuk/ca-certificates/./2023-05-30/share: unable to copy extended attributes to /usr/local/Cellar/ca-certificates/./2023-05-30/share: No such file or directory
cp: /usr/local/Cellar/ca-certificates/./2023-05-30/share/ca-certificates: No such file or directory
cp: /private/tmp/d20230604-29041-desbuk/ca-certificates/./2023-05-30/share/ca-certificates: unable to copy extended attributes to /usr/local/Cellar/ca-certificates/./2023-05-30/share/ca-certificates: No such file or directory
cp: /usr/local/Cellar/ca-certificates/./2023-05-30/share/ca-certificates/cacert.pem: No such file or directory
cp: utimensat: /usr/local/Cellar/ca-certificates/./2023-05-30/share/ca-certificates: No such file or directory
cp: chown: /usr/local/Cellar/ca-certificates/./2023-05-30/share/ca-certificates: No such file or directory
cp: chmod: /usr/local/Cellar/ca-certificates/./2023-05-30/share/ca-certificates: No such file or directory
cp: chflags: /usr/local/Cellar/ca-certificates/./2023-05-30/share/ca-certificates: No such file or directory
cp: /private/tmp/d20230604-29041-desbuk/ca-certificates/./2023-05-30/share/ca-certificates: unable to copy ACL to /usr/local/Cellar/ca-certificates/./2023-05-30/share/ca-certificates: No such file or directory
cp: utimensat: /usr/local/Cellar/ca-certificates/./2023-05-30/share: No such file or directory
cp: chown: /usr/local/Cellar/ca-certificates/./2023-05-30/share: No such file or directory
cp: chmod: /usr/local/Cellar/ca-certificates/./2023-05-30/share: No such file or directory
cp: chflags: /usr/local/Cellar/ca-certificates/./2023-05-30/share: No such file or directory
cp: /private/tmp/d20230604-29041-desbuk/ca-certificates/./2023-05-30/share: unable to copy ACL to /usr/local/Cellar/ca-certificates/./2023-05-30/share: No such file or directory
cp: utimensat: /usr/local/Cellar/ca-certificates/./2023-05-30: No such file or directory
cp: chown: /usr/local/Cellar/ca-certificates/./2023-05-30: No such file or directory
cp: chmod: /usr/local/Cellar/ca-certificates/./2023-05-30: No such file or directory
cp: chflags: /usr/local/Cellar/ca-certificates/./2023-05-30: No such file or directory
cp: /private/tmp/d20230604-29041-desbuk/ca-certificates/./2023-05-30: unable to copy ACL to /usr/local/Cellar/ca-certificates/./2023-05-30: Permission denied
cp: utimensat: /usr/local/Cellar/ca-certificates/.: Permission denied
cp: /private/tmp/d20230604-29041-desbuk/ca-certificates/.: unable to copy ACL to /usr/local/Cellar/ca-certificates/.: Bad file descriptor
Error: Failure while executing; `/usr/bin/env cp -pR /private/tmp/d20230604-29041-desbuk/ca-certificates/. /usr/local/Cellar/ca-certificates` exited with 1. Here's the output:
cp: /private/tmp/d20230604-29041-desbuk/ca-certificates/.: unable to copy extended attributes to /usr/local/Cellar/ca-certificates/.: Bad file descriptor
cp: /usr/local/Cellar/ca-certificates/./2023-05-30: Permission denied
cp: /private/tmp/d20230604-29041-desbuk/ca-certificates/./2023-05-30: unable to copy extended attributes to /usr/local/Cellar/ca-certificates/./2023-05-30: Permission denied
cp: /usr/local/Cellar/ca-certificates/./2023-05-30/.brew: No such file or directory
cp: /private/tmp/d20230604-29041-desbuk/ca-certificates/./2023-05-30/.brew: unable to copy extended attributes to /usr/local/Cellar/ca-certificates/./2023-05-30/.brew: No such file or directory
cp: /usr/local/Cellar/ca-certificates/./2023-05-30/.brew/ca-certificates.rb: No such file or directory
cp: utimensat: /usr/local/Cellar/ca-certificates/./2023-05-30/.brew: No such file or directory
cp: chown: /usr/local/Cellar/ca-certificates/./2023-05-30/.brew: No such file or directory
cp: chmod: /usr/local/Cellar/ca-certificates/./2023-05-30/.brew: No such file or directory
cp: chflags: /usr/local/Cellar/ca-certificates/./2023-05-30/.brew: No such file or directory
cp: /private/tmp/d20230604-29041-desbuk/ca-certificates/./2023-05-30/.brew: unable to copy ACL to /usr/local/Cellar/ca-certificates/./2023-05-30/.brew: No such file or directory
cp: /usr/local/Cellar/ca-certificates/./2023-05-30/share: No such file or directory
cp: /private/tmp/d20230604-29041-desbuk/ca-certificates/./2023-05-30/share: unable to copy extended attributes to /usr/local/Cellar/ca-certificates/./2023-05-30/share: No such file or directory
cp: /usr/local/Cellar/ca-certificates/./2023-05-30/share/ca-certificates: No such file or directory
cp: /private/tmp/d20230604-29041-desbuk/ca-certificates/./2023-05-30/share/ca-certificates: unable to copy extended attributes to /usr/local/Cellar/ca-certificates/./2023-05-30/share/ca-certificates: No such file or directory
cp: /usr/local/Cellar/ca-certificates/./2023-05-30/share/ca-certificates/cacert.pem: No such file or directory
cp: utimensat: /usr/local/Cellar/ca-certificates/./2023-05-30/share/ca-certificates: No such file or directory
cp: chown: /usr/local/Cellar/ca-certificates/./2023-05-30/share/ca-certificates: No such file or directory
cp: chmod: /usr/local/Cellar/ca-certificates/./2023-05-30/share/ca-certificates: No such file or directory
cp: chflags: /usr/local/Cellar/ca-certificates/./2023-05-30/share/ca-certificates: No such file or directory
cp: /private/tmp/d20230604-29041-desbuk/ca-certificates/./2023-05-30/share/ca-certificates: unable to copy ACL to /usr/local/Cellar/ca-certificates/./2023-05-30/share/ca-certificates: No such file or directory
cp: utimensat: /usr/local/Cellar/ca-certificates/./2023-05-30/share: No such file or directory
cp: chown: /usr/local/Cellar/ca-certificates/./2023-05-30/share: No such file or directory
cp: chmod: /usr/local/Cellar/ca-certificates/./2023-05-30/share: No such file or directory
cp: chflags: /usr/local/Cellar/ca-certificates/./2023-05-30/share: No such file or directory
cp: /private/tmp/d20230604-29041-desbuk/ca-certificates/./2023-05-30/share: unable to copy ACL to /usr/local/Cellar/ca-certificates/./2023-05-30/share: No such file or directory
cp: utimensat: /usr/local/Cellar/ca-certificates/./2023-05-30: No such file or directory
cp: chown: /usr/local/Cellar/ca-certificates/./2023-05-30: No such file or directory
cp: chmod: /usr/local/Cellar/ca-certificates/./2023-05-30: No such file or directory
cp: chflags: /usr/local/Cellar/ca-certificates/./2023-05-30: No such file or directory
cp: /private/tmp/d20230604-29041-desbuk/ca-certificates/./2023-05-30: unable to copy ACL to /usr/local/Cellar/ca-certificates/./2023-05-30: Permission denied
cp: utimensat: /usr/local/Cellar/ca-certificates/.: Permission denied
cp: /private/tmp/d20230604-29041-desbuk/ca-certificates/.: unable to copy ACL to /usr/local/Cellar/ca-certificates/.: Bad file descriptor

lbdv@Air-Dmitrij ~ % pip3 install kivy[base] kivy_examples
zsh: no matches found: kivy[base]
lbdv@Air-Dmitrij ~ % mkdir my_kivy_app
cd my_kivy_app

lbdv@Air-Dmitrij my_kivy_app % touch game.py
nano game.py


  UW PICO 5.09                                 File: game.py                                  Modified  

from random import random
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.graphics import Color, Ellipse, Line


class MyPaintWidget(Widget):

    def on_touch_down(self, touch):
        color = (random(), 1, 1)
        with self.canvas:
            Color(*color, mode='hsv')
            d = 30.
            Ellipse(pos=(touch.x - d / 2, touch.y - d / 2), size=(d, d))
            touch.ud['line'] = Line(points=(touch.x, touch.y))

    def on_touch_move(self, touch):
        touch.ud['line'].points += [touch.x, touch.y]


class MyPaintApp(App):

    def build(self):
        parent = Widget()
        self.painter = MyPaintWidget()
        clearbtn = Button(text='Clear')
        clearbtn.bind(on_release=self.clear_canvas)
        parent.add_widget(self.painter)
        parent.add_widget(clearbtn)
        return parent

    def clear_canvas(self, obj):
        self.painter.canvas.clear()

if __name__ == '__main__':
    MyPaintApp().run()





















                                        [ Unknown Command: ^S ]                                         
^G Get Help      ^O WriteOut      ^R Read File     ^Y Prev Pg       ^K Cut Text      ^C Cur Pos       
^X Exit          ^J Justify       ^W Where is      ^V Next Pg       ^U UnCut Text    ^T To Spell      
