##
# sd-svs-config
# ========
#
# Moves files into place on sd-svs
#
#

# populate config.json for sd-svs. This contains the journalist_key_fingerprint
# used to encrypt replies

{% import_json "sd/config.json" as d %}

install-securedrop-proxy-yaml-config:
  file.managed:
    - name: /home/user/.securedrop_client/config.json
    - source: salt://sd/sd-svs/config.json.j2
    - template: jinja
    - context:
        submission_fpr: {{ d.submission_key_fpr}}
    - user: user
    - group: user
    - mode: 0600
    - makedirs: True
