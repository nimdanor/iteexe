# ===========================================================================
# eXe 
# Copyright 2004-2005, University of Auckland
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
# ===========================================================================

import sys
import logging
import gettext
from exe.webui import common
from exe.webui.block          import Block
from exe.webui.blockfactory   import g_blockFactory

log = logging.getLogger(__name__)
_   = gettext.gettext


# ===========================================================================
class TitleBlock(Block):
    """
    TitleBlock is for rendering node titles
    """
    def __init__(self, node):
        self.node = node

    def processDone(self, request):
        if "title%d"%self.id in request.args:
            self.node.title = request["title%d"%self.id]

    def renderEdit(self):
        """
        Returns an XHTML string with the form element for editing this block
        """
        html  = "<div>\n"
        html += common.textInput("title%d"%self.id, self.node.title)
        html += common.submitButton("done%d"%self.id, _("Done"))
        html += "</div>\n"


    def renderView(self):
        """
        Returns an XHTML string for viewing this block
        """
        html  = "<div>\n"
        html += "<h1 class=\"title\">" + self.node.title + "</h1>"
        html += common.submitButton("edit"+self.node.idStr(), _("Edit"))
        html += "</div>\n"
        return html

# ===========================================================================
