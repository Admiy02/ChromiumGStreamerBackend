# Copyright 2015 The Chromium Authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

{
  'variables': {
    'scheduler_common_sources': [
      'common/scheduler_switches.cc',
      'common/scheduler_switches.h',
    ],
    'scheduler_sources': [
      'child/cancelable_closure_holder.cc',
      'child/cancelable_closure_holder.h',
      'child/child_scheduler.h',
      'child/idle_helper.cc',
      'child/idle_helper.h',
      'child/nestable_single_thread_task_runner.h',
      'child/null_idle_task_runner.cc',
      'child/null_idle_task_runner.h',
      'child/null_task_queue.cc',
      'child/null_task_queue.h',
      'child/null_worker_scheduler.cc',
      'child/null_worker_scheduler.h',
      'child/pollable_thread_safe_flag.cc',
      'child/pollable_thread_safe_flag.h',
      'child/prioritizing_task_queue_selector.cc',
      'child/prioritizing_task_queue_selector.h',
      'child/scheduler_helper.cc',
      'child/scheduler_helper.h',
      'child/scheduler_task_runner_delegate.h',
      'child/scheduler_task_runner_delegate_impl.cc',
      'child/scheduler_task_runner_delegate_impl.h',
      'child/single_thread_idle_task_runner.cc',
      'child/single_thread_idle_task_runner.h',
      'child/task_queue.h',
      'child/task_queue_manager.cc',
      'child/task_queue_manager.h',
      'child/task_queue_selector.h',
      'child/web_scheduler_impl.cc',
      'child/web_scheduler_impl.h',
      'child/webthread_base.cc',
      'child/webthread_base.h',
      'child/webthread_impl_for_worker_scheduler.cc',
      'child/webthread_impl_for_worker_scheduler.h',
      'child/worker_scheduler.cc',
      'child/worker_scheduler.h',
      'child/worker_scheduler_impl.cc',
      'child/worker_scheduler_impl.h',
      'renderer/deadline_task_runner.cc',
      'renderer/deadline_task_runner.h',
      'renderer/null_renderer_scheduler.cc',
      'renderer/null_renderer_scheduler.h',
      'renderer/renderer_scheduler.cc',
      'renderer/renderer_scheduler.h',
      'renderer/renderer_scheduler_impl.cc',
      'renderer/renderer_scheduler_impl.h',
      'renderer/renderer_web_scheduler_impl.cc',
      'renderer/renderer_web_scheduler_impl.h',
      'renderer/webthread_impl_for_renderer_scheduler.cc',
      'renderer/webthread_impl_for_renderer_scheduler.h',
      'scheduler_export.h',
    ],
    'scheduler_test_support_sources': [
      'test/lazy_scheduler_message_loop_delegate_for_tests.cc',
      'test/lazy_scheduler_message_loop_delegate_for_tests.h',
    ],
  },
}
