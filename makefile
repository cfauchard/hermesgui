################################################################################
# start configuration
#
ROOT=/Users/Christophe/Projets/hermesgui
site=hermesgui.intranet.itnovem.com
#
# end configuration
################################################################################


DJANGO_PROJECT=hermesgui
USER=hermesgui
PORT=443
all=dirs static

all: $(all)

clean:
	rm -rf $(ROOT)/www/static
	rm -rf $(ROOT)/apache
	rm -rf $(ROOT)/logs

dirs:
	[ -d $(ROOT)/apache ] || mkdir $(ROOT)/apache
	[ -d $(ROOT)/logs ] || mkdir $(ROOT)/logs
	[ -d $(ROOT)/www/static ] || mkdir -p $(ROOT)/www/static

static: 
	(cd $(ROOT)/django; python manage.py collectstatic --no-input)

apache: dirs static
	mod_wsgi-express setup-server \
	--log-directory $(ROOT)/logs/ \
	--document-root $(ROOT)/www/ \
	--server-root $(ROOT)/apache \
	--working-directory $(ROOT)/django \
	--user $(USER) \
	--server-root $(ROOT)/apache/ \
	--entry-point $(ROOT)/django/$(DJANGO_PROJECT)/wsgi.py \
	--https-port $(PORT) \
	--https-only \
	--server-name hermesgui.intranet.itnovem.com \
	--ssl-certificate-file $(ROOT)/ssl/$(site).crt \
	--ssl-certificate-key-file $(ROOT)/ssl/$(site).key
