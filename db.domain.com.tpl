;
; BIND data file for {{ fqdn }}
;
$TTL	604800
@	IN	SOA	{{ fqdn }} {{ email_address }} (
			      2		; Serial
			 604800		; Refresh
			  86400		; Retry
			2419200		; Expire
			 604800 )	; Negative Cache TTL
;
@	IN	NS	ns.{{ fqdn }}
@	IN	A	{{ ip_address }}
@	IN	AAAA	::1
