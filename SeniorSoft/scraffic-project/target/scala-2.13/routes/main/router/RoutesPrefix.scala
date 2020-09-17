// @GENERATOR:play-routes-compiler
// @SOURCE:/Users/marcusmousavi/SeniorSoft/scraffic-project/conf/routes
// @DATE:Wed Sep 16 23:38:43 CDT 2020


package router {
  object RoutesPrefix {
    private var _prefix: String = "/"
    def setPrefix(p: String): Unit = {
      _prefix = p
    }
    def prefix: String = _prefix
    val byNamePrefix: Function0[String] = { () => prefix }
  }
}
