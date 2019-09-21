if [ $1 ]
then
    rm secret -rf
fi
if [ ! -f secret/key.pem ] || [ ! -f secret/certificate.crt ]
then
    if [ ! $1 ]
    then
        echo "Usage: ./generate_cert <domain>"
        exit 1
    fi
    echo "\n\tGenerating new Certificate\n"
    if [ ! -d secret ]
    then
        mkdir secret
    fi
    echo "\n\n\n\n\n$1\n\n" | openssl req -newkey rsa:2048 -nodes -keyout secret/key.pem -x509 -days 365 -out secret/certificate.crt
    else
    echo "\n\tCert found, not re-generating"
fi