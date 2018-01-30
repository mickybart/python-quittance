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

from datetime import datetime
from dateutil.relativedelta import relativedelta
import locale

class DateHelper():
    """Permit to easily manage dates"""
    
    def setLocale(self, locale_env):
        """Set the LC_TIME
        
        Args:
            locale_env (str): locale
        """
        locale.setlocale(locale.LC_TIME, locale_env)

    def getToday(self):
        """Get the current date
        
        Returns:
            datetime: The current date
        """
        return datetime.now()

    def getBeginOfMonth(self, current : datetime):
        """Get the 1st of the month
        
        Args:
            current (datetime): a date
            
        Returns:
            datetime: The 1st of the month
        """
        return datetime(current.year, current.month, 1)

    def getBeginOfThisMonth(self):
        """Get the 1st of this month
        
        Returns:
            datetime: The 1st of this month
        """
        return self.getBeginOfMonth(self.getToday())

    def getEndOfMonth(self, current : datetime):
        """Get the end of the month
        
        Args:
            current (datetime): a date
            
        Returns:
            datetime: The end of the month
        """
        return self.getBeginOfMonth(current) + relativedelta(months=1, days=-1)

    def getEndOfThisMonth(self):
        """Get the end of this month
        
        Returns:
            datetime: The end of this month
        """
        return self.getEndOfMonth(self.getToday())

    def strMonthYear(self, current: datetime):
        """Get the Month Year string
        
        Args:
            current (datetime): a date
            
        Returns:
            str: The Month and Year (eg: Janvier 2018)
        """
        s = current.strftime("%B %Y")
        return s[0].upper() + s[1:]
    
    def strShort(self, current: datetime, format="%d/%m/%Y"):
        """Get a short string for the date
        
        Args:
            current (datetime): a date
        
        Keyword Arguments:
            format (str): a string converter for datetime.strftime
            
        Returns:
            str: The date in string (eg: 30/01/2018)
        """
        return current.strftime(format)

