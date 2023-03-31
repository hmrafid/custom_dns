zone "{{ domain }}" {
    type master;
    file "/etc/bind/db.{{ domain }}";
};

zone "{{first_three_octets_of_ip}}.in-addr.arpa" {
    type master;
    file "/etc/bind/db.{{first_octet_of_ip}}";
};
