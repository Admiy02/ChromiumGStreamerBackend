// Copyright 2015 The Chromium Authors. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

#include "base/callback.h"
#include "components/proximity_auth/cryptauth/mock_cryptauth_client.h"

namespace proximity_auth {

MockCryptAuthClient::MockCryptAuthClient() {
}

MockCryptAuthClient::~MockCryptAuthClient() {
}

MockCryptAuthClientFactory::MockCryptAuthClientFactory(MockType mock_type)
    : mock_type_(mock_type) {
}

MockCryptAuthClientFactory::~MockCryptAuthClientFactory() {
}

scoped_ptr<CryptAuthClient> MockCryptAuthClientFactory::CreateInstance() {
  scoped_ptr<MockCryptAuthClient> client;
  if (mock_type_ == MockType::MAKE_STRICT_MOCKS)
    client.reset(new testing::StrictMock<MockCryptAuthClient>());
  else
    client.reset(new testing::NiceMock<MockCryptAuthClient>());

  FOR_EACH_OBSERVER(Observer, observer_list_,
                    OnCryptAuthClientCreated(client.get()));
  return client.Pass();
}

void MockCryptAuthClientFactory::AddObserver(Observer* observer) {
  observer_list_.AddObserver(observer);
}

void MockCryptAuthClientFactory::RemoveObserver(Observer* observer) {
  observer_list_.RemoveObserver(observer);
}

}  // namespace proximity_auth
