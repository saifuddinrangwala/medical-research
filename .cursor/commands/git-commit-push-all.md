Commit and push all current repository changes to the configured remote.

Execution rules:
- Ask for a commit message if the user has not provided one in the same prompt.
- Run `git status` first and summarize what will be committed.
- Stage all changes with `git add -A`.
- Commit with the provided message.
- Push to `origin` on the current branch.
- If push fails due to upstream not set, push with `-u origin HEAD`.
- If there are no changes to commit, report that and stop.

Safety rules:
- Do not modify git config.
- Do not use force push unless the user explicitly asks.
- Do not include ignored/private files.
