// Copyright 2014 The Chromium Authors. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

#ifndef IOS_WEB_NET_COOKIE_NOTIFICATION_BRIDGE_H_
#define IOS_WEB_NET_COOKIE_NOTIFICATION_BRIDGE_H_

#include "base/mac/scoped_nsobject.h"
#include "base/macros.h"
#include "base/threading/thread_checker.h"

@class NSNotification;

namespace web {

// CookieNotificationBridge listens to
// NSHTTPCookieManagerCookiesChangedNotification on the main thread and re-sends
// it to the cookie store on the IO thread.
class CookieNotificationBridge {
 public:
  CookieNotificationBridge();
  ~CookieNotificationBridge();

 private:
  void OnNotificationReceived(NSNotification* notification);
  base::scoped_nsprotocol<id> observer_;
  base::ThreadChecker thread_checker_;

  DISALLOW_COPY_AND_ASSIGN(CookieNotificationBridge);
};

}  // namespace web

#endif  // IOS_WEB_NET_COOKIE_NOTIFICATION_BRIDGE_H_
