# Blog

Source code for my personal blog.

## Commands

### Start server

```sh
docker-compose up
```

Visit [http://localhost:3000/](http://localhost:3000/)

### Build static pages

```sh
docker-compose exec app sh -c "hugo -D -d docs/"
```

## License

CC BY-SA 4.0
