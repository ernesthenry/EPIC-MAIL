class Group:
    """Model class for groups"""

    def __init(self, group_id, group_name, role):
        self.group_id = group_id,
        self.group_name = group_name,
        self.role = role

    def group_dict(self):
        return {
            'group_id': self.group_id,
            'group_name':self.group_name,
            'role':self.role
        }
        
        
