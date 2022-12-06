package main

import (
	"context"
	"encoding/json"
	"fmt"
	"io"
	"log"
	"net"
	"net/http"

	"github.com/kadirkaragoz/blogserver/blog"
	"google.golang.org/grpc"
)

const port = "localhost:8001"
const base_url = "https://jsonplaceholder.typicode.com"

func main() {
	srv := grpc.NewServer()
	listen, err := net.Listen("tcp", port)
	if err != nil {
		panic(err)
	}
	blog.RegisterBlogServiceServer(srv, &BlogService{})
	log.Println("Starting server...")
	panic(srv.Serve(listen))
}

type BlogService struct {
	blog.UnimplementedBlogServiceServer
}

func (s *BlogService) QueryPost(ctx context.Context, req *blog.PostRequest) (*blog.PostResponse, error) {
	url := fmt.Sprintf("%v/posts/%v", base_url, req.Id)
	resp, err := http.Get(url)
	if err != nil {
		return nil, err
	}
	defer resp.Body.Close()

	jsonBody, err := io.ReadAll(resp.Body)
	if err != nil {
		return nil, err
	}
	respData := blog.PostResponse{}
	if err := json.Unmarshal(jsonBody, &respData); err != nil {
		return nil, err
	}
	return &respData, nil
}

func (s *BlogService) ListPosts(ctx context.Context, req *blog.ListPostRequest) (*blog.ListPostResponse, error) {
	url := fmt.Sprintf("%v/posts", base_url)
	resp, err := http.Get(url)
	if err != nil {
		return nil, err
	}
	defer resp.Body.Close()

	jsonBody, err := io.ReadAll(resp.Body)
	if err != nil {
		return nil, err
	}
	postlist := []*blog.PostResponse{}
	respData := new(blog.ListPostResponse)
	if err := json.Unmarshal(jsonBody, &postlist); err != nil {
		return nil, err
	}
	respData.Posts = postlist
	return respData, nil
}
