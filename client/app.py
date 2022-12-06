import json
from flask import Flask
from flask import jsonify
from flask import Response

app = Flask(__name__)

import grpc
import blog_pb2 as blog_messages
import blog_pb2_grpc as blog_service
from google.protobuf import empty_pb2


@app.route('/api/v1/posts', methods=['GET'])
def home():
    channel = grpc.insecure_channel('localhost:8001')
    stub = blog_service.BlogServiceStub(channel)
    list_post_response = stub.ListPosts(empty_pb2.Empty())
    post_list = [{"id": post.id, "body": post.body, "title": post.title} for post in list_post_response.posts]
    return Response(json.dumps(post_list))


@app.route("/api/v1/posts/<int:id>", methods=['GET'])
def posts(id):
    channel = grpc.insecure_channel('localhost:8001')
    stub = blog_service.BlogServiceStub(channel)
    req = blog_messages.PostRequest(id=id)
    res = stub.QueryPost(req)
    return jsonify({
        "id": res.id,
        "title": res.title,
        "body": res.body
    })


if __name__ == "__main__":
    app.run()
