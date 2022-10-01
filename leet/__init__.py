# https://leetcode.com/problemset/all/
import logging
import unittest

from typing import List

INT_MAX = 2**31 - 1
INT_MIN = -(2**31)


def get_logger(logger_name, create_file=False):
    log = logging.getLogger(logger_name)
    log.setLevel(level=logging.INFO)

    # create formatter and add it to the handlers
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )

    if create_file:
        # create file handler for logger.
        fh = logging.FileHandler("SPOT.log")
        fh.setLevel(level=logging.DEBUG)
        fh.setFormatter(formatter)
    # reate console handler for logger.
    ch = logging.StreamHandler()
    ch.setLevel(level=logging.DEBUG)
    ch.setFormatter(formatter)

    # add handlers to logger.
    if create_file:
        log.addHandler(fh)

    log.addHandler(ch)
    return log


LOGGER = get_logger("LEET")


class CaseCollection:
    def __init__(self):
        self.case_dicts_by_descr = {}

    def add_case(self, descr: str, inputs: List, expected_result):
        self.case_dicts_by_descr[descr] = {
            "inputs": inputs,
            "expected_result": expected_result,
        }

    def items(self):
        return self.case_dicts_by_descr.items()


class TestCase(unittest.TestCase):
    def run_cases(self, cases: CaseCollection, solver_obj):
        solver_name = str(solver_obj.__class__)
        if not solver_obj.IMPLEMENTED:
            LOGGER.warning(f"Not Implemented - Skipping Tests: {solver_name}")
            return
        failed_cases = []
        for descr, case in cases.items():
            expected = case["expected_result"]
            inputs = case["inputs"]
            info = {
                "descr": descr,
                "case": case,
            }
            LOGGER.info("running case: {}".format(info))
            result = solver_obj.solve(*inputs)
            info = {
                "result": result,
                "descr": descr,
                "case": case,
            }
            if result != expected:
                failed_cases.append(info)
        self.assertEqual([], failed_cases, f"Failed cases for {solver_name}")
