# Dasturchi bilan bog'lanish T.me/Shoirjon_No1
 

import base64, codecs
magic = 'aW1wb3J0IGFzeW5jaW8KZnJvbSB0ZWxldGhvbiBpbXBvcnQgVGVsZWdyYW1DbGllbnQsIGV2ZW50cywgc3luYwppbXBvcnQgemV1cy5jbGllbnQKZnJvbSB0aW1lIGltcG9ydCBzbGVlcApjbGllbnQgPSB6ZXVzLmNsaWVudC5jbGllbnQKCkBldmVudHMucmVnaXN0ZXIoZXZlbnRzLk5ld01lc3NhZ2UocGF0dGVybj0iLnNub3ciLCBvdXRnb2luZz1UcnVlKSkKYXN5bmMgZGVmIHNub3cobWVzc2FnZSk6Cglhd2FpdCBtZXNzYWdlLmVkaXQoJ+KYge+4j/CfjKjimIHvuI/wn4yo4piB77iP8J+MqOKYge+4j/CfjKjimIHvuI/wn4yo4piB77iPXG5cblxuXG5cblxu4puE77iP4piD77iP4puE77iP4piD77iP4puE77iP4piD77iP4puE77iP4piD77iP4puE77iP4piD77iP4puE77iPJykgCglhd2FpdCBhc3luY2lvLnNsZWVwKDAuNzUpIAoJYXdhaXQgbWVzc2FnZS5lZGl0KCfimIHvuI/wn4yo4piB77iP8J+MqOKYge+4j/CfjKjimIHvuI/wn4yo4piB77iP8J+MqOKYge+4j1xuICAgIOKdhO+4jyAgICDinYTvuI8gICAgIOKdhO+4jyAgICAg4p2E77iPICAgICDinYTvuI8gICDinYTvuI9cblxuXG5cblxu4puE77iP4piD77iP4puE77iP4piD77iP4puE77iP4piD77iP4puE77iP4piD77iP4puE77iP4piD77iP4puE77iPJykgCglhd2FpdCBhc3luY2lvLnNsZWVwKDAuNzUpIAoJYXdhaXQgbWVzc2FnZS5lZGl0KCfimIHvuI/wn4yo4piB77iP8J+MqOKYge+4j/CfjKjimIHvuI/wn4yo4piB77iP8J+MqOKYge+4j1xuICAgIOKdhO+4jyAgICDinYTvuI8gICAgIOKdhO+4jyAgICAg4p2E77iPICAgICDinYTvuI8gICDinYTvuI9cbuKdhO+4jyAgICDinYTvuI8gICAg4p2E77iPICAgIOKdhO+4jyAgICDinYTvuI8gICAg4p2E77iPICAgICAgIFxuXG5cblxu4puE77iP4piD77iP4puE77iP4piD77iP4pu'
love = 'R77vC4cvQ77vC4chR77vC4cvQ77vC4chR77vC4cvQ77vC4chR77vCWlxtPtyuq2ScqPOup3yhL2yiYaAfMJIjXQNhAmHcVNbWLKqunKDtoJImp2SaMF5yMTy0XPpt4cvO77vC8W+ZdBXLtr+4w/PswXwvzVUihV/ja4lb4cvO77vC8W+ZdBXLtr+4w/PswXwvzVUihV9povNtVBXquB+4wlNtVPQvaLGihV8tVPNtVBXquB+4wlNtVPNt4c2R77vCVPNtVPQvaLGihV8tVPQvaLGihV9pohXquB+4wlNtVPQvaLGihV8tVPNt4c2R77vCVPNtVBXquB+4wlNtVPQvaLGihV8tVPNt4c2R77vCVPNtVPNtVSkhVPNtVBXquB+4wlNtVPQvaLGihV8tVPNt4c2R77vCVPNtVBXquB+4wlNtVPQvaLGihV8tVPNt4c2R77vCVPNtVPOpoykhKT7vz4GihV/vzVCihV/vz4GihV/vzVCihV/vz4GihV/vzVCihV/vz4GihV/vzVCihV/vz4GihV/vzVCihV/vz4GihV8aXFNXPJS3LJy0VTSmrJ5wnJ8hp2kyMKNbZP43AFxtPtyuq2ScqPOgMKAmLJqyYzIxnKDbW+XLtr+4w/PswXwvzVUihV/ja4lb4cvO77vC8W+ZdBXLtr+4w/PswXwvzVUihV/ja4lb4cvO77vCKT4tVPNt4c2R77vCVPNtVBXquB+4wlNtVPNt4c2R77vCVPNtVPQvaLGihV8tVPNtVBXquB+4wlNtVBXquB+4w1kh4c2R77vCVPNtVBXquB+4wlNtVPQvaLGihV8tVPNt4c2R77vCVPNtVBXquB+4wlNtVPQvaLGihV8tVPNtVPNtKT4tVPNt4c2R77vCVPNtVBXquB+4wlNtVPQvaLGihV8tVPNt4c2R77vCVPNtVBXquB+4wlNtVPQvaLGihV8tVPNtVSkh4c2R77vCVPNtVBXquB+4wlNtVPQvaLGihV8tVPNt4c2R77vCVPNtVBXquB+4wlNtVPQvaLGihV8tVPNtVSkhKT7vz4GihV/vzVCihV/vz4GihV/vzVCihV/vz4GihV/vzVCihV/vz4GihV/vzVCihV/vz4GihV/vzVCihV/vz4GihV8aXFNXPJS3LJy0VTSmrJ5wnJ8hp2kyMKNbZP43AFxtPtyuq2ScqPOgMKAmLJqyYzIxnK'
god = 'QoJ+KYge+4j/CfjKjimIHvuI/wn4yo4piB77iP8J+MqOKYge+4j/CfjKjimIHvuI/wn4yo4piB77iPXG4gICAg4p2E77iPICAgIOKdhO+4jyAgICAg4p2E77iPICAgICDinYTvuI8gICAgIOKdhO+4jyAgIOKdhO+4j1xu4p2E77iPICAgIOKdhO+4jyAgICDinYTvuI8gICAg4p2E77iPICAgIOKdhO+4jyAgICDinYTvuI8gICAgICAgXG4gICAg4p2E77iPICAgIOKdhO+4jyAgICDinYTvuI8gICAg4p2E77iPICAgIOKdhO+4jyAgICDinYTvuI8gICAgIFxu4p2E77iPICAgIOKdhO+4jyAgICDinYTvuI8gICAg4p2E77iPICAgIOKdhO+4jyAgICDinYTvuI8gICAgIFxuICDinYTvuI8gICAgICDinYTvuI8gICAg4p2E77iPICDinYTvuI8gICAgICDinYTvuI8gIOKdhO+4jyBcbuKbhO+4j+KYg++4j+KbhO+4j+KYg++4j+KbhO+4j+KYg++4j+KbhO+4j+KYg++4j+KbhO+4j+KYg++4j+KbhO+4jycpICAKCWF3YWl0IGFzeW5jaW8uc2xlZXAoMS4yNSkgCglhd2FpdCBtZXNzYWdlLmVkaXQoJ+KYge+4j/CfjKjimIHvuI/wn4yo4piB77iP8J+MqOKYge+4j/CfjKjimIHvuI/wn4yo4piB77iPXG5cbuKdhO+4jyAgICDinYTvuI8gICAg4p2E77iPICAgIOKdhO+4jyAgICDinYTvuI8gICAg4p2E77iPICAgICAgIFxuICAgIOKdhO+4jyAgICDinYTvuI8gICAg4p2E77iPICAgIOKdhO+4jyAgICDinYTvuI8gICAg4p2E77iPICAgICBcbuKdhO+4jyAgICDinYTvuI8gICAg4p2E77iPICAgIOKdhO+4jyAgICDinYTvuI8gICAg4p2E77iPICAgICBcbiAg4p2E77iPICAgICAg4p2E77iPICAgIOKdhO+4jyAg4p2E77iPICAgICAg4p2E77iPICDinYTvuI8gIFxu4puE77iP4piD77iP4puE77iP4piD77iP4puE77iP4piD77iP4puE77iP4piD77iP4puE77iP4piD77iP4puE77iPJykgCglhd2FpdCBhc3luY2lvLnNsZ'
destiny = 'JIjXQNhAmHcVNbWLKqunKDtoJImp2SaMF5yMTy0XPsvzVUihV/ja4lb4cvO77vC8W+ZdBXLtr+4w/PswXwvzVUihV/ja4lb4cvO77vC8W+ZdBXLtr+4w1khKT5povNtVPQvaLGihV8tVPNt4c2R77vCVPNtVBXquB+4wlNtVPQvaLGihV8tVPNt4c2R77vCVPNtVBXquB+4wlNtVPNtKT7vaLGihV8tVPNt4c2R77vCVPNtVBXquB+4wlNtVPQvaLGihV8tVPNt4c2R77vCVPNtVBXquB+4wlNtVPNtKT4tVBXquB+4wlNtVPNtVBXquB+4wlNtVPQvaLGihV8tVBXquB+4wlNtVPNtVBXquB+4wlNt4c2R77vCVSkh4chR77vC4cvQ77vC4chR77vC4cvQ77vC4chR77vC4cvQ77vC4chR77vC4cvQ77vC4chR77vC4cvQ77vC4chR77vCWlxtPtyuq2ScqPOup3yhL2yiYaAfMJIjXQNhAmHcVNbWLKqunKDtoJImp2SaMF5yMTy0XPsvzVUihV/ja4lb4cvO77vC8W+ZdBXLtr+4w/PswXwvzVUihV/ja4lb4cvO77vC8W+ZdBXLtr+4w1khKT5poykh4c2R77vCVPNtVBXquB+4wlNtVPQvaLGihV8tVPNt4c2R77vCVPNtVBXquB+4wlNtVPQvaLGihV8tVPNtVSkhVPQvaLGihV8tVPNtVPQvaLGihV8tVPNt4c2R77vCVPQvaLGihV8tVPNtVPQvaLGihV8tVBXquB+4wlOpohXouB+4w+XLt++4w+XouB+4w+XLt++4w+XouB+4w+XLt++4w+XouB+4w+XLt++4w+XouB+4w+XLt++4w+XouB+4wlpcVNbWLKqunKDtLKA5ozAcol5moTIypPtjYwp1XFNXPJS3LJy0VT1yp3AuM2HhMJEcqPta4cvO77vC8W+ZdBXLtr+4w/PswXwvzVUihV/ja4lb4cvO77vC8W+ZdBXLtr+4w/PswXwvzVUihV9poykhKT5poykhVPQvaLGihV8tVPNtVPQvaLGihV8tVPNt4c2R77vCVPQvaLGihV8tVPNtVPQvaLGihV8tVBXquB+4wlOpohXouB+4w+XLt++4w+XouB+4w+XLt++4w+XouB+4w+XLt++4w+XouB+4w+XLt++4w+XouB+4w+XLt++4w+XouB+4wlpc'
joy = '\x72\x6f\x74\x31\x33'
trust = eval('\x6d\x61\x67\x69\x63') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x6c\x6f\x76\x65\x2c\x20\x6a\x6f\x79\x29') + eval('\x67\x6f\x64') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x64\x65\x73\x74\x69\x6e\x79\x2c\x20\x6a\x6f\x79\x29')
eval(compile(base64.b64decode(eval('\x74\x72\x75\x73\x74')),'<string>','exec'))