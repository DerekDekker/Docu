server {
    listen 443; #暴露给外部访问的端口
    server_name api.holehub.org;
        charset utf-8;
    location / {
        include uwsgi_params;
        uwsgi_pass 127.0.0.1:8995; #外部访问8996就转发到内部8997
        client_max_body_size 50m;
    }
    ssl on;
    ssl_certificate /etc/nginx/conf.d/full_chain.pem;
    ssl_certificate_key /etc/nginx/conf.d/private.key;
}
