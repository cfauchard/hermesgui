#
# fill only Common Name (eg, fully qualified host name) [] for the csr generation 
#

openssl=/usr/bin/openssl
validity=3650
length=2048
site=hermesgui.intranet.itnovem.com
all=$(site).crt $(site).key

all: $(all)

$(site).crt: $(site).csr
	$(openssl) x509 -req -days $(validity) -in $(site).csr -signkey $(site).key -out $(site).crt 

$(site).csr: $(site).key
	$(openssl) req -new -key $(site).key -out $(site).csr 

$(site).key:
	$(openssl) genrsa -out $(site).key $(length)

clean:
	rm -f *.key *.csr *.crt
