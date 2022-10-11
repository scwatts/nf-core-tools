import logging
from pathlib import Path

from nf_core.components.components import Components


log = logging.getLogger(__name__)


class ModuleCommand(Components):
    """
    Base class for the 'nf-core modules' commands
    """

    def __init__(self, dir, remote_url=None, branch=None, no_pull=False):
        super().__init__("modules", dir, remote_url, branch, no_pull)

    def get_local_modules(self):
        """
        Get the local modules in a pipeline
        """
        local_module_dir = Path(self.dir, "modules", "local")
        return [str(path.relative_to(local_module_dir)) for path in local_module_dir.iterdir() if path.suffix == ".nf"]
