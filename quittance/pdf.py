# Copyright (c) 2018 mickybart
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#     http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from fpdf import FPDF, HTMLMixin
from .datehelper import DateHelper

class PDF(FPDF, HTMLMixin):
    """Export receipt as a PDF"""
    
    def output_pdf(self, get_quittance, paid, today = None, begin = None, end = None, filename = None):
        """Write a pdf receipt on disk
        
        Args:
            get_quittance (function): a compatible function to get the receipt
            paid (str): short string for paid date
        
        Keyword Arguments:
            today (datetime): today
            begin (datetime): begin date for the receipt
            end (datetime): end date for the receipt
            filename (str): pdf filename
        """
        
        # Add a page
        self.add_page()
        
        # Set dates if needed
        datehelper = DateHelper()
        
        if not today:
            today = datehelper.getToday()
        if not begin:
            begin = datehelper.getBeginOfMonth(today)
        if not end:
            end = datehelper.getEndOfMonth(today)

        # Get receipt in HTML
        html = get_quittance(datehelper.strMonthYear(today),
                           datehelper.strShort(begin),
                           datehelper.strShort(end),
                           paid,
                           datehelper.strShort(today))
        
        # Write the receipt
        self.write_html(html)
        
        # Store the receipt
        if not filename:
            filename = "quittance-%s.pdf" % (datehelper.strMonthYear(today).lower().replace(" ", "-"))
        self.output(filename, 'F')
