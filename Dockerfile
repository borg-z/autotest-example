from joyzoursky/python-chromedriver:3.7-selenium
RUN pip3 install pytest-selenium pytest-rerunfailures pytest-ordering pytest-sugar  allure-pytest pytest-xdist\
    && apt-get update ;apt-get -y install default-jre \
    && apt-get clean

RUN curl -o allure.tgz -Ls https://dl.bintray.com/qameta/generic/io/qameta/allure/allure/2.7.0/allure-2.7.0.tgz \
    && tar -zxvf allure.tgz -C /opt/ && ln -s /opt/allure-2.7.0/bin/allure /usr/bin/allure
WORKDIR /tests
