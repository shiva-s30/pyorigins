import pathlib as pl

WORKSPACE_PATH = pl.Path(__file__).parent.parent.resolve()
SRC_DIR_PATH = pl.Path(WORKSPACE_PATH, "src")
TEST_DIR_PATH = pl.Path(WORKSPACE_PATH, "tests")
REPORT_DIR_PATH = pl.Path(WORKSPACE_PATH, "report")

print(WORKSPACE_PATH, SRC_DIR_PATH, TEST_DIR_PATH)