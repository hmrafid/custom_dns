options {
	directory "/var/cache/bind";

	forwarders {
		{{ forwarder_dns }};
	};

	dnssec-validation auto;

	listen-on-v6 { any; };
};
