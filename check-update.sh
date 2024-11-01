#!/bin/sh
# sombok changed its versioning scheme from time based to semantic,
# so we need to get rid of versions like "2011.4" even if they
# appear "newer" than 2.4.0
git ls-remote --tags https://github.com/hatukanezumi/sombok.git 2>/dev/null|awk '{ print $2; }' |sed -e "s,refs/tags/,,;s,_,.,g;s,-,.,g;s,^v\.,,;s,^v,,;s,^sombok\.,," |grep -vE '^[0-9][0-9][0-9][0-9]' |grep -vE '(alpha|beta|gamma|RC)' |sort -V |tail -n1
