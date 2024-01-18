from app.core.task.stats.ToolStats import ToolStats


class FuzzerStats:
    time_to_bug: int = 0
    line_coverage: int = 0
    total_lines: int = 0
    branch_coverage: int = 0
    total_branches: int = 0
    executions: int = 0

    def get_dict(self):
        summary = {
            "time to bug": self.time_to_bug,
            "line coverage": self.line_coverage,
            "total lines": self.total_lines,
            "branch covarege": self.branch_coverage,
            "total branches": self.total_branches,
            "executions": self.executions,
        }
        return summary


class FuzzToolStats(ToolStats):
    fuzzing_stats: FuzzerStats

    def __init__(self):
        self.fuzzing_stats = FuzzerStats()
        super(FuzzToolStats, self).__init__()

    def get_dict(self):
        res = super(FuzzToolStats, self).get_dict()
        res["details"]["fuzz_stats"] = self.fuzzing_stats.get_dict()
        return res

    def write(self, printer, prefix=""):
        printer(
            "{1} time to bug: {0} second(s)\n".format(
                self.fuzzing_stats.time_to_bug, prefix
            )
        )
        printer("{1} executions: {0}\n".format(self.fuzzing_stats.executions, prefix))
        printer(
            "{1} lines covered: {0} out of {2}\n".format(
                self.fuzzing_stats.line_coverage, prefix, self.fuzzing_stats.total_lines
            )
        )
        printer(
            "{1} branches covered: {0} out of {2}\n".format(
                self.fuzzing_stats.branch_coverage,
                prefix,
                self.fuzzing_stats.total_branches,
            )
        )
        super(FuzzToolStats, self).write(printer, prefix)
