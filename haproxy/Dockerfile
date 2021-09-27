FROM haproxy:2.2-alpine
COPY ./haproxy.cfg/haproxy.cfg /usr/local/etc/haproxy/haproxy.cfg
COPY ./haproxy.cfg/haproxy.cfg/whitelist_agent.lst /usr/local/etc/haproxy/whitelist_agent.lst
COPY ./haproxy.cfg/haproxy.cfg/blacklist_agent.lst /usr/local/etc/haproxy/blacklist_agent.lst
EXPOSE 80



