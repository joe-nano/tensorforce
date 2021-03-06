# Copyright 2020 Tensorforce Team. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================

import unittest

from test.unittest_base import UnittestBase


class TestObjectives(UnittestBase, unittest.TestCase):

    def test_deterministic_policy_gradient(self):
        self.start_tests(name='deterministic-policy-gradient')

        objective = dict(type='deterministic_policy_gradient')
        baseline_policy = dict(network=dict(type='auto', size=7, depth=1, rnn=1))
        baseline_objective = dict(type='value', value='action')
        self.unittest(
            actions=dict(type='float', shape=(), min_value=1.0, max_value=2.0), objective=objective,
            baseline_policy=baseline_policy, baseline_objective=baseline_objective
        )

    def test_plus(self):
        self.start_tests(name='plus')

        # TODO: should be objective1='value'
        objective = dict(type='plus', objective1='policy_gradient', objective2='policy_gradient')
        self.unittest(objective=objective)

    def test_policy_gradient(self):
        self.start_tests(name='policy-gradient')

        objective = dict(type='policy_gradient')
        self.unittest(objective=objective)

        objective = dict(type='policy_gradient', importance_sampling=True)
        self.unittest(objective=objective)

        objective = dict(type='policy_gradient', clipping_value=1.0)
        self.unittest(objective=objective)

        objective = dict(type='policy_gradient', importance_sampling=True, clipping_value=0.2)
        self.unittest(objective=objective)

        objective = dict(type='policy_gradient', early_reduce=True)
        self.unittest(objective=objective)

    def test_value(self):
        self.start_tests(name='value')

        objective = dict(type='value', value='state')
        self.unittest(objective=objective)

        # TODO: action value doesn't exist for Beta
        policy = dict(network=dict(type='auto', size=8, depth=1, rnn=2))
        objective = dict(type='value', value='action')
        self.unittest(policy=policy, objective=objective)

        objective = dict(type='value', huber_loss=1.0)
        self.unittest(objective=objective)

        objective = dict(type='value', early_reduce=True)
        self.unittest(objective=objective)
