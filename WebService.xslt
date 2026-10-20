<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

    <xsl:template match="/"> <!-- "/" as default ? -->

  <html>
            <body>

                <b>
                    <h1>RestAPI</h1>
                </b> <!-- RESTAPI heading-->

                <table border="1">
                    <tr bgcolor="#fff8dc">
                        <th>Method</th>
                        <th>Parameter List</th>
                        <th>Return type</th>
                        <th>Exception Count</th>
                    </tr>
                    <xsl:for-each select="interface/abstract_method">
                        <tr>
                            <td>
                                <xsl:value-of select="@name" />
                            </td>
                            <td>
                                <xsl:for-each select="parameters//parameter">
                                    <xsl:value-of select="." />
                                  <xsl:text>:</xsl:text>
                                  <xsl:value-of
                                        select="@type" />
                                  <xsl:if test="position() != last()"> , </xsl:if>
                                </xsl:for-each>
                                <xsl:text> (Total : </xsl:text>
                                <xsl:value-of select="count(parameters/parameter)" />
                                <xsl:text> ) </xsl:text>
                            </td>
                            <td>
                                <xsl:value-of select="return" />
                            </td>
                            <td>
                                <xsl:value-of select="count(exceptions/exception)" />
                            </td>

                        </tr>
                    </xsl:for-each>
                </table>


                <b>
                    <p> Total methods: <xsl:value-of select="count(interface/abstract_method/@name)" /></p>
                </b>

            </body>
        </html>
    </xsl:template>

</xsl:stylesheet>