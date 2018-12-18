all: httpd client
<<<<<<< HEAD
LIBS = -lpthread #-lsocket
httpd: httpd.c
	gcc -W -Wall -o httpd httpd.c -lpthread

client: simpleclient.c
	gcc -W -Wall -o httpd httpd.c -lpthread
=======
LIBS = -pthread #-lsocket
httpd: httpd.c
	gcc -g -W -Wall $(LIBS) -o $@ $<

client: simpleclient.c
	gcc -W -Wall -o $@ $<
>>>>>>> 1d0ddd61a7c75c809c58cca3fda0cd3972235bd4
clean:
	rm httpd
