## Usage:

### Scan a Directory

`dagger call scan-dir --path test/`

### Scan a File

`dagger call scan-file --path test/main.tf`

Both scans return a `dagger.Container` and can be further interacted with.

## Options

Additional arguments can be passed to either scan with the `--args` option.

Scan a directory and only fail on `high` severity findings:
`dagger call scan-dir --path test/ --args "--fail-on,high"`

Scan a file and exclude a specific query:
`dagger call scan-file --path test/main.tf --args "--exclude-queries,fd632aaf-b8a1-424d-a4d1-0de22fd3247a"`

KICS provide documentation and examples on scan command options: [Scan Command Options](https://docs.kics.io/latest/commands/#scan_command_options)
