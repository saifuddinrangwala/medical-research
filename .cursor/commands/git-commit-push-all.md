Commit and push all current repository changes to the configured remote.

Execution rules:
- If commit message is not provided, generate one from the change summary:
  - inspect `git status` + `git diff --stat` + staged file list
  - produce a concise message reflecting the primary intent of the change
- Run `git status` first and summarize what will be committed.
- Stage all changes with `git add -A`.
- Commit with the provided or generated message.
- Checkout `main` before push workflow.
- If current branch is not `main`, merge current branch into `main`.
- Push directly to `origin main`.
- If there are no changes to commit, report that and stop.
- Do not create or suggest pull requests in this command.

Safety rules:
- Do not modify git config.
- Do not use force push unless the user explicitly asks.
- Do not include ignored/private files.
