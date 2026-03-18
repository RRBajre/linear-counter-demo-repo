#!/bin/zsh
set -euo pipefail

export SSL_CERT_FILE=/opt/homebrew/etc/ca-certificates/cert.pem
export HEX_CACERTS_PATH=/opt/homebrew/etc/ca-certificates/cert.pem

cd /Users/raj1.bajre/Documents/Symphony/symphony/elixir

mix run -e 'SymphonyElixir.CLI.main(["--i-understand-that-this-will-be-running-without-the-usual-guardrails", "/Users/raj1.bajre/Documents/Symphony/linear-counter-demo-repo/WORKFLOW.md"])'
