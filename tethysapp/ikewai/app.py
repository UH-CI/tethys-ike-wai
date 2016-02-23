from tethys_sdk.base import TethysAppBase, url_map_maker


class IkeWai(TethysAppBase):
    """
    Tethys app class for Ike Wai.
    """

    name = 'Ike Wai'
    index = 'ikewai:home'
    icon = 'ikewai/images/icon.gif'
    package = 'ikewai'
    root_url = 'ikewai'
    color = '#1abc9c'
    description = 'Place a brief description of your app here.'
    enable_feedback = False
    feedback_emails = []

        
    def url_maps(self):
        """
        Add controllers
        """
        UrlMap = url_map_maker(self.root_url)

        url_maps = (UrlMap(name='home',
                           url='ikewai',
                           controller='ikewai.controllers.home'),
        )

        return url_maps