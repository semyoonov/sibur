# 904
# POST /upload/2 HTTP/1.0
# Content-Length: 801
# Host: xxxxxxxxx.dev.example.com
# User-Agent: xxx (shell 1)

# ^.^........W.j^1^.^.^.²..^^.i.^B.P..-!(.l/Y..V^.      ...L?...S'NR.^^vm...3Gg@s...d'.\^.5N.$NF^,.Z^.aTE^.
# ._.[..k#L^ƨ`\RE.J.<.!,.q5.F^՚iΔĬq..^6..P..тH.`..i2
# .".uuzs^^F2...Rh.&.U.^^..J.P@.A......x..lǝy^?.u.p{4..g...m.,..R^.^.^......].^^.^J...p.ifTF0<.s.9V.o5<..%!6ļS.ƐǢ..㱋....C^&.....^.^y...v]^YT.1.#K.ibc...^.26...   ..7.
# b.$...j6.٨f...W.R7.^1.3....K`%.&^..d..{{      l0..^\..^X.g.^.r.(!.^^...4.1.$\ .%.8$(.n&..^^q.,.Q..^.D^.].^.R9.kE.^.$^.I..<..B^..^.h^^C.^E.|....3o^.@..Z.^.s.$[v.



#!/usr/bin/python3
import requests
import random

def print_request(request):
    headers_str = ''.join('{0}: {1}\r\n'.format(k, v) for k, v in request.headers.items())
    req_template_w_entity_body = (
          "%s %s HTTP/1.1\r\n"
          "%s\r\n"
          "%s\r\n"
    )
    req = req_template_w_entity_body % (str(request.method), str(request.url), str(headers_str), str(request.body))
    ammo_template = (
        "%d\n"
        "%s"
    )
    return ammo_template % (len(req), req)

def create_post_requests(cnt, host, port, namespace, headers):
    all_data = b''
    for i in range(cnt):
        priority = random.choice(['WARN', 'CRIT', 'INFO'])
        desc = random.choice(['kek', 'lol', 'gooooooaaaaaal'])
        msg = random.choice(['a', 'b', 'timohaturboloh'])
        tp = random.choice([1, 2, 3, 5, 6, 8])
        payload = f'priority={priority}&description={desc}&message={msg}&type={tp}'
        req = requests.Request(
            'POST',
            'http://{host}:{port}{namespace}'.format(
                host = host,
                port = port,
                namespace = namespace,
            ),
            headers = headers,
            data = payload,
        )
        prepared = req.prepare()
        all_data += print_request(prepared).encode()
    return all_data

if __name__ == '__main__':
    headers = {
        'Host': '51.250.48.50:5000',
        'Cache-Control': 'max-age=0',
        'Connection': 'close',
        'Cookie': 'session=.eJyljsEKwjAMhl8l5FwEr3sDwZM3kTFim3WB2srS7jL27quCINibp_CT74NvxWEMpBMrdrcVIdeDD1Ylz2jwmgpEZgc5wZ0hJO_rkIj9Zn7pC3vRPFOWFEGLtfUzlmDgGZj0rVf30JbPycu31aZeQRMtXGs4fnpSyW36FBcK4sDO7DhmoaB_go3K3mBRngdx2B23Hf9YcjQ.Zx_2yw.cKE5qRz1JhcStHedDRNoJG7tpTs',
        'User-Agent': 'Tank',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Upgrade-Insecure-Requests': '1',
    }

    res = create_post_requests(100, '51.250.48.50', '5000', '/submit', headers)
    with open('ammo.txt', 'wb') as f:
        f.write(res)
