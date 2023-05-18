# check-code-scanning-analysis

1. Run this [GH CLI](https://cli.github.com/) tool to get a list of repos in your org: `gh repo list <YOUR ORG> --json nameWithOwner --limit 1000 > ./repo-list.json`. This will create a file with all of the repos the script will query.
2. Update `check.py` to include your GH API token
3. Run `check.py` to query the analysis endpoint for each repo.  Only the repos with errors will be output.
