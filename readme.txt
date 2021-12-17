############################################################################
##############################IRP auto clicker##############################
############################################################################

--------------------------------------------------------------------------------------------
windows cmd to start chrome on a specific port in a seperated user profile:

---
cd C:\Program Files (x86)\Google\Chrome\Application

chrome.exe --remote-debugging-port=8989 --user-data-dir="T:\Selenium\IRP_Clicker_profile"
--------------------------------------------------------------------------------------------
chrome driver path:
---
'C:/webdrivers/chromedriver.exe'

--------------------------------------------------------------------------------------------
(chrome_port) chrome was started at port:

http://localhost:8989
--------------------------------------------------------------------------------------------
button(find appointment button) id:
---
id = "btSrch4Apps"
--------------------------------------------------------------------------------------------
some text messages shown on the IRP page:
---
No appointment(s) are currently available
---
There was a problem finding available appointment slots.
Please try reloading this page.
---
There was a problem completing the action. If you were creating a new appointment your booking has NOT been confirmed
An unexpected error has occurred, please try again
--------------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------------
important html elements on the page:
---
/html/body/form/div/div[2]/div/div[3]/div[4]/div

<div id="dvAppOptions" class="table-responsive" style="display: block;">
    <table class="table"><tbody>
            <tr>
                <td></td><td>No appointment(s) are currently available</td>
            </tr>
        </tbody>
    </table>
</div>
------
/html/body/form/div/div[2]/div/div[3]/div[4]/div/div/table/tbody/tr/td[1]/button

<button type="button" class="btn btn-success" onclick="bookit('94E8CD1A1782AF60802587AC005993B4')">
    Book This
</button>
--------------------------------------------------------------------------------------------


