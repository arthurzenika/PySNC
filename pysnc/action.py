class Action:

    def __init__(self, client, table, sys_id=None):
        self._client = client
        self._table = table

    def list_banner_actions(self, view, related_list, parent_table):
        """
        Retrieve list banner actions for the table

        :param view: The current view
        :param related_list: The current r elate list
        :param parent_table: THe parent table, if the list is related
        """
        #GET
        f"{self._table}/for_list_banner"

    def list_bottom_buttons(self, view):
        """
        Retrieve actions for list bottom buttons
        :param view: The current view
        """
        #GET
        f"{self._table}/for_list_button"

    def list_choice_list(self, view):
        """
        Retrieve actions for list choice list
        :param view: The current view
        """
        #GET
        f"{self._table}/for_list_choice_list"

    def list_context_menu(self, sys_id, view):
        """
        Retrieve list conext menu actiosn for a specific record
        :param sys_id: record to use
        :param view: The current view
        """
        #GET
        f"{self._table}/for_list_context_menu"
        params = dict(sysparm_sys_id=sys_id, sysparm_view=view)

    def list_links(self, view='default'):
        """
        Retrieve list link actions for a table
        :param view: The current view
        """
        #GET
        f"{self._table}/for_list_links"

    def execute(self, action_id, payload={}):
        """
        execute a ui action
        :param payload: what does this even do?
        """
        #POST
        f"{action_id}"
        params = dict(sysparm_table=record.table, sysparm_sys_id=record.sys_id)
