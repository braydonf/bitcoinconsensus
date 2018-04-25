{
  "targets": [
	{
	  "target_name": "bitcoinconsensus",
	  "defines": [
		"HAVE_CONFIG_H=1"
	  ],
	  "sources": [
		"./bindings.cc",
		"./bitcoin/src/script/bitcoinconsensus.cpp",
		"./bitcoin/src/script/bitcoinconsensus.h",
		"./bitcoin/src/script/interpreter.cpp",
		"./bitcoin/src/script/interpreter.h",
		"./bitcoin/src/script/script.cpp",
		"./bitcoin/src/script/script.h",
		"./bitcoin/src/pubkey.cpp",
		"./bitcoin/src/pubkey.h",
		"./bitcoin/src/hash.cpp",
		"./bitcoin/src/hash.h",
		"./bitcoin/src/primitives/transaction.cpp",
		"./bitcoin/src/primitives/transaction.h",
		"./bitcoin/src/utilstrencodings.cpp",
		"./bitcoin/src/utilstrencodings.h",
		"./bitcoin/src/uint256.cpp",
		"./bitcoin/src/uint256.h",
		"./bitcoin/src/crypto/hmac_sha512.cpp",
		"./bitcoin/src/crypto/hmac_sha512.h",
		"./bitcoin/src/crypto/hmac_sha256.cpp",
		"./bitcoin/src/crypto/hmac_sha256.h",
		"./bitcoin/src/crypto/ripemd160.cpp",
		"./bitcoin/src/crypto/ripemd160.h",
		"./bitcoin/src/crypto/sha1.cpp",
		"./bitcoin/src/crypto/sha1.h",
		"./bitcoin/src/crypto/sha256.cpp",
		"./bitcoin/src/crypto/sha256_sse4.cpp",
		"./bitcoin/src/crypto/sha256.h",
		"./bitcoin/src/crypto/sha512.cpp",
		"./bitcoin/src/crypto/sha512.h",
		"./bitcoin/src/secp256k1/src/secp256k1.c",
		"./bitcoin/src/secp256k1/include/secp256k1.h",
	  ],
	  'conditions': [
		['OS=="mac"', {
		  'xcode_settings': {
			'GCC_ENABLE_CPP_EXCEPTIONS': 'YES'
		  }
		}],
	  ],
	 'cflags': [
	   '-Wno-unused-function'
	 ],
	 'cflags_cc': [
	   '-fexceptions',
	   '-std=c++11'
	  ],
	  'link_settings': {
		'libraries': [
		  '-lgmp'
		]
	  },
	  "include_dirs" : [
		".",
		"./bitcoin/src",
		"./bitcoin/src/secp256k1",
		"./bitcoin/src/secp256k1/include",
		"<!(node -e \"require('nan')\")"
	  ],
	}
  ]
}
