const PROTO_PATH = __dirname + '/chat_service.proto';

const parseArgs = require('minimist');
const grpc = require('@grpc/grpc-js');
const protoLoader = require('@grpc/proto-loader');
const packageDefinition = protoLoader.loadSync(
  PROTO_PATH,
  {
    keepCase: true,
    longs: String,
    enums: String,
    defaults: true,
    oneofs: true
  });
const chat_service_proto = grpc.loadPackageDefinition(packageDefinition).chatService;

function main() {
  const argv = parseArgs(process.argv.slice(2), {
    string: 'target'
  });
  let target;
  if (argv.target) {
    target = argv.target;
  } else {
    target = 'localhost:50051';
  }
  const client = new chat_service_proto.ChatService(target,
    grpc.credentials.createInsecure());
  let user;
  if (argv._.length > 0) {
    user = argv._[0];
  } else {
    user = 'world';
  }
  const hello = "hello";
  client.RepeatRequest(hello, function (err, response) {
    console.log(response);
  });
}

main();