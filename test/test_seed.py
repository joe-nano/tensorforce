# Copyright 2018 Tensorforce Team. All Rights Reserved.
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

import numpy as np

from test.unittest_base import UnittestBase
from tensorforce.agents import Agent
from tensorforce.environments import Environment


class TestSeed(UnittestBase, unittest.TestCase):

    require_observe = True

    def test_seed(self):
        self.start_tests()

        states = dict(
            int_state=dict(type='int', shape=(2,), num_values=4),
            float_state=dict(type='float', shape=(2,)),
        )
        actions = dict(
            int_action=dict(type='int', shape=(2,), num_values=4),
            float_action=dict(type='float', shape=(2,)),
        )

        agent, environment = self.prepare(states=states, actions=actions, exploration=0.5, seed=0)

        agent.initialize()

        states = environment.reset()
        # print(states['int_state'])
        # print(states['float_state'])
        self.assertTrue(expr=np.allclose(a=states['int_state'], b=np.asarray([3, 1])))
        self.assertTrue(
            expr=np.allclose(a=states['float_state'], b=np.asarray([-2.36958691, 0.8640523]))
        )

        actions = agent.act(states=states)
        # print(actions['int_action'])
        # print(actions['float_action'])
        self.assertTrue(expr=np.allclose(a=actions['int_action'], b=np.asarray([2, 3])))
        self.assertTrue(
            expr=np.allclose(a=actions['float_action'], b=np.asarray([-0.12984827, 0.46496633]))
        )

        states, terminal, reward = environment.execute(actions=actions)
        updated = agent.observe(terminal=terminal, reward=reward)
        # print(states['int_state'])
        # print(states['float_state'])
        # print(terminal, reward)
        self.assertTrue(expr=np.allclose(a=states['int_state'], b=np.asarray([0, 1])))
        self.assertTrue(
            expr=np.allclose(a=states['float_state'], b=np.asarray([1.48838294, 0.32484357]))
        )
        self.assertEqual(first=terminal, second=False)
        self.assertEqual(first=reward, second=0.515908805880605)
        self.assertFalse(expr=updated)

        actions = agent.act(states=states)
        # print(actions['int_action'])
        # print(actions['float_action'])
        self.assertTrue(expr=np.allclose(a=actions['int_action'], b=np.asarray([0, 1])))
        self.assertTrue(
            expr=np.allclose(a=actions['float_action'], b=np.asarray([-0.28552642, 0.10683993]))
        )

        states, terminal, reward = environment.execute(actions=actions)
        updated = agent.observe(terminal=terminal, reward=reward)
        # print(states['int_state'])
        # print(states['float_state'])
        # print(terminal, reward)
        self.assertTrue(expr=np.allclose(a=states['int_state'], b=np.asarray([0, 2])))
        self.assertTrue(
            expr=np.allclose(a=states['float_state'], b=np.asarray([-2.36417382, 0.02033418]))
        )
        self.assertEqual(first=terminal, second=False)
        self.assertEqual(first=reward, second=-0.15885683833831)
        self.assertFalse(expr=updated)

        actions = agent.act(states=states)
        # print(actions['int_action'])
        # print(actions['float_action'])
        self.assertTrue(expr=np.allclose(a=actions['int_action'], b=np.asarray([0, 3])))
        self.assertTrue(
            expr=np.allclose(a=actions['float_action'], b=np.asarray([-0.6319358, 0.767941]))
        )

        states, terminal, reward = environment.execute(actions=actions)
        updated = agent.observe(terminal=terminal, reward=reward)
        # print(states['int_state'])
        # print(states['float_state'])
        # print(terminal, reward)
        self.assertTrue(expr=np.allclose(a=states['int_state'], b=np.asarray([2, 2])))
        self.assertTrue(
            expr=np.allclose(a=states['float_state'], b=np.asarray([-1.91440763, 0.07323557]))
        )
        self.assertEqual(first=terminal, second=False)
        self.assertEqual(first=reward, second=-0.4821664994140733)
        self.assertFalse(expr=updated)

        actions = agent.act(states=states)
        # print(actions['int_action'])
        # print(actions['float_action'])
        self.assertTrue(expr=np.allclose(a=actions['int_action'], b=np.asarray([2, 2])))
        self.assertTrue(
            expr=np.allclose(a=actions['float_action'], b=np.asarray([0.17954004, 1.453299]))
        )


        states, terminal, reward = environment.execute(actions=actions)
        updated = agent.observe(terminal=terminal, reward=reward)
        # print(states['int_state'])
        # print(states['float_state'])
        # print(terminal, reward)
        self.assertTrue(expr=np.allclose(a=states['int_state'], b=np.asarray([1, 0])))
        self.assertTrue(
            expr=np.allclose(a=states['float_state'], b=np.asarray([-1.13980246, 0.78495752]))
        )
        self.assertEqual(first=terminal, second=True)
        self.assertEqual(first=reward, second=0.02254944273721704)
        self.assertFalse(expr=updated)