// TODO: add mongo host/db name here
grails {
    mongodb {
        host = "mongo-0.mongo"
        port = 27017
        databaseName = "platform_db"
        engine = "mapping"
        options {
            connectionsPerHost = 30
        }
    }
}

// TODO: set to hostname
tomcat_hostname = "http://localhost:8080"


grails.serverURL = "${tomcat_hostname}"
grails.app.context = "/"
grails.plugin.springsecurity.active = true
grails.plugin.springsecurity.cas.active = true
grails.plugin.springsecurity.cas.loginUri = '/login'
grails.plugin.springsecurity.cas.serviceUrl = "${grails.serverURL}/j_spring_cas_security_check"
grails.plugin.springsecurity.cas.serverUrlPrefix = '${grails.serverURL}/auth/'
grails.plugin.springsecurity.logout.afterLogoutUrl = "${grails.serverURL}/auth/logout?service=${grails.serverURL}/"
