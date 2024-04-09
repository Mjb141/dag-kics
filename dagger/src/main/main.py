from typing import Annotated
from typing_extensions import Doc
import dagger
from dagger import dag, function, object_type


@object_type
class DagKics:
    def base(self) -> dagger.Container:
        return dag.container().from_("checkmarx/kics:latest")

    @function
    def scan_dir(
        self,
        path: Annotated[dagger.Directory, Doc("Path to directory you want to scan")],
        args: Annotated[
            list[str], Doc("Additional arguments to pass to the KICS scan command")
        ] = [],
    ) -> dagger.Container:
        "Scan a Directory with KICS"
        return (
            self.base()
            .with_directory("/src", path)
            .with_exec(["scan", "-p", "/src", "-o", "/src/"] + args)
        )

    @function
    async def scan_file(
        self,
        path: Annotated[dagger.File, Doc("Path to file you want to scan")],
        args: Annotated[
            list[str], Doc("Additional arguments to pass to the KICS scan command")
        ] = [],
    ) -> dagger.Container:
        "Scan a File with KICS"
        file_name = await path.name()
        return (
            self.base()
            .with_file(f"/src/{file_name}", path)
            .with_exec(["scan", "-p", f"/src/{file_name}", "-o", "/src/"] + args)
        )
