#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Test the 'serve' module of the hwrt package."""

import nose
from flask import Flask
from flask_bootstrap import Bootstrap

# hwrt modules
import hwrt.serve as serve
import hwrt.utils as utils


# Tests
def execution_test():
    """Just test if the function is executable."""
    results = [{'symbolnr': 32,
                'semantics': '\\alpha',
                'probability': 0.67},
               {'symbolnr': 124,
                'semantics': '\\propto',
                'probability': 0.25}]
    serve.show_results(results)
    serve.get_json_result(results)
    serve.fix_writemath_answer(results)
    serve.index()


def interactive_heartbeat_test():
    """Test the 'heartbeat' function of the '/interactive' route."""
    template_path = utils.get_template_folder()

    app = Flask(__name__, template_folder=template_path)
    Bootstrap(app)
    app.config.from_object(__name__)
    with app.test_request_context('/interactive?heartbeat=Peter'):
        a = serve.interactive()
        nose.tools.assert_equal(a, "Peter")
