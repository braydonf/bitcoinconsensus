#include <node.h>
#include <node_buffer.h>
#include <nan.h>
#include <bitcoinconsensus.h>

using namespace v8;
using namespace std;

void VerifyScript(const v8::FunctionCallbackInfo<Value>& args) {
	if (!node::Buffer::HasInstance(args[0])) {
		return Nan::ThrowTypeError("First argument should be a Buffer.");
	}

	if (!node::Buffer::HasInstance(args[1])) {
		return Nan::ThrowTypeError("Second argument should be a Buffer.");
	}

	unsigned char *scriptPubKey = (unsigned char *) node::Buffer::Data(args[0]);
	unsigned int scriptPubKeyLen = (unsigned int) node::Buffer::Length(args[0]);

	const unsigned char *txTo = (unsigned char *) node::Buffer::Data(args[1]);
	unsigned int txToLen = (unsigned int)node::Buffer::Length(args[1]);

	unsigned int nIn = args[2]->NumberValue();
	unsigned int flags = args[3]->NumberValue();

	bitcoinconsensus_error err;

	int valid = bitcoinconsensus_verify_script(scriptPubKey, scriptPubKeyLen, txTo, txToLen, nIn, flags, &err);

	if ((int)err) {
		Local<Value> errVal =  Nan::New<Number>((int)err);
		return Nan::ThrowError(errVal);
	}

	args.GetReturnValue().Set(Nan::New<Number>(valid));
}

void Version(const v8::FunctionCallbackInfo<Value>& args) {
	Isolate* isolate = args.GetIsolate();
	unsigned int version = bitcoinconsensus_version();
	Local<Number> version_number = Number::New(isolate, version);
	args.GetReturnValue().Set(version_number);
}

void init(Handle<Object> exports) {
	NODE_SET_METHOD(exports, "verifyScript", VerifyScript);
	NODE_SET_METHOD(exports, "version", Version);
}

NODE_MODULE(bitcoinconsensus, init);
