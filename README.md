# bitcoinconsensus

Node.js bindings to Bitcoin Core's script verification [libbitcoinconsensus](https://github.com/bitcoin/bitcoin/blob/master/doc/shared-libraries.md)

This library is experimental, so use at your own risk.

## Build

There are a couple of rough edges when installing the library, as there are dependencies on the build system from Bitcoin Core, such as the need for `config/bitcoin-config.h` and `ecmult_static_context.h`, so it's necessary to build Bitcoin Core before building the bindings.

```bash
git clone git@github.com:braydonf/node-libbitcoinconsensus.git
cd node-libbitcoinconsensus
git submodule init
git submodule update
pushd bitcoin
./autogen.sh
./configure --disable-tests --disable-wallet --disable-bench --disable-zmq --disable-tests --disable-gui-tests --with-gui=no --with-miniupnpc=no
make -j 8
popd
npm install
npm test
```

## Usage

```js

'use strict';

var bitcoinconsensus = require('bitcoinconsensus');

// the transaction spending an output
var txTo = new Buffer('01000000015884e5db9de218238671572340b207ee85b628074e7e467096c267266baf77a4000000006a4730440220340f35055aceb14250e4954b23743332f671eb803263f363d1d7272f1d487209022037a0eaf7cb73897ba9069fc538e7275c5ae188e934ae47ca4a70453b64fc836401210234257444bd3aead2b851bda4288d60abe34095a2a8d49aff1d4d19773d22b32cffffffff01a0860100000000001976a9147821c0a3768aa9d1a37e16cf76002aef5373f1a888ac00000000', 'hex');

// the previous unspent output script
var scriptPubKey = new Buffer('76a9144621d47f08fcb1e6be0b91144202de7a186deade88ac', 'hex');

// the input index that is spending the scriptPubKey
var nIn = 0;

var valid = bitcoinconsensus.verifyScript(scriptPubKey, txTo, nIn);

// valid will equal 0 (false) or 1 (true)
console.log(valid);

// the version of libbitcoinconsensus
var version = bitcoinconsensus.version();
console.log(version);


```

## API

bitconconsensus.version()
-----------------------------
Get the version of the libbitcoinconsensus library

**Parameters**

none

**Returns**: String representing the version of the library.

bitcoinconsensus.verifyScript(scriptPubKey, txTo, nIn, flags)
-----------------------------
Verify the script according to the buffers sent in (scriptPubKey)

**Parameters**
* scriptPubKey - `Buffer`
* txTo -  `Buffer`
* nInt - `integer`
* flags - `integer`

**Returns**: integer representing whether the script was valid (1) or not valid (0).

**Throws**: String exception when an exception is handled by the native library.

License
-----------------------------
MIT
