FROM nginx:latest

RUN rm /etc/nginx/conf.d/default.conf

COPY ./docker/nginx/django.conf /etc/nginx/conf.d/

#RUN openssl dhparam -out /etc/nginx/conf.d/dhparam.pem 1024


