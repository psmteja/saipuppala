@callback_manager_home.callback(
    [
        Output("measures_info", "children"),
        Output("measures_info", "style"),
        Output("measures_infos", "children"),
        Output("measures_infos", "style"),
        Output("warranty_claim", "children"),
        Output("warranty_claim", "style"),
        Output("DTAC_ccms", "children"),
        Output("DTAC_ccms", "style"),
        Output("elips_history", "children"),
        Output("elips_history", "style"),
        Output("pip_history", "children"),
        Output("pip_history", "style"),
        Output("optionCodes", "children"),
        Output("optionCodes", "style"),
        Output("componentSerialNumber", "children"),
        Output("componentSerialNumber", "style"),
        Output("factoryOptions", "children"),
        Output("factoryOptions", "style"),
        Output("firmware_info", "children"),
        Output("firmware_info", "style"),
        Output("prod_info", "children"),
        Output("prod_info", "style"),
        Output("EA_info", "children"),
        Output("EA_info", "style"),
        Output("SA_info", "children"),
        Output("SA_info", "style"),
        Output("jdcp_info", "children"),
        Output("jdcp_info", "style"),
        Output("progress-load", "children")
    ],
    [Input('submit-val', 'n_clicks'),
     Input('session-data', 'modified_timestamp'),
     State('session-data', 'data')],
)
def update_measurement_product_dealer_panels(n_clicks, ts, data):
    if ts is None:
        raise PreventUpdate

    data = data or {}
    status = {}
    # native_pin
    if n_clicks > 0 and len(str(data.get('native_pin', 0))) == 17:
        try:
            df = DataFrame(data_load.measurements_index(str(data.get('mach_id', 0))))
            if df.shape[0] > 0:
                measures = dash_table_fetch_two_col(df)
                status['measures'] = 'block'
            else:
                measures = ""
                status['measures'] = 'none'

            df = DataFrame(data_load.warranty_index(str(data.get('mach_id', 0))))
            if df.shape[0] > 0:
                warranty = dash_table_fetch(df)
                status['warranty'] = 'block'
            else:
                warranty = ""
                status['warranty'] = 'none'

            df = DataFrame(data_load.warranty_claim_history(str(data.get('native_pin', 0))))
            if df.shape[0] > 0:
                warranty_claim = dash_table_fetch(df)
                status['warranty_claim'] = 'block'
            else:
                warranty_claim = ""
                status['warranty_claim'] = 'none'

            df = DataFrame(data_load.dtac_ccms(str(data.get('native_pin', 0))))
            if df.shape[0] > 0:
                DTAC_ccms = dash_table_fetch(df)
                status['DTAC_ccms'] = 'block'
            else:
                DTAC_ccms = ""
                status['DTAC_ccms'] = 'none'

            df = DataFrame(data_load.elips_history(str(data.get('native_pin', 0))))
            if df.shape[0] > 0:
                elips_history = dash_table_fetch(df)
                status['elips_history'] = 'block'
            else:
                elips_history = ""
                status['elips_history'] = 'none'

            df = DataFrame(data_load.pip_history(str(data.get('native_pin', 0))))
            if df.shape[0] > 0:
                pip_history = dash_table_fetch_two_col(df)
                status['pip_history'] = 'block'
            else:
                pip_history = ""
                status['pip_history'] = 'none'

            df = DataFrame(data_load.optionCodes(str(data.get('native_pin', 0))))
            if df.shape[0] > 0:
                optionCodes = dash_table_fetch(df)
                status['optionCodes'] = 'block'
            else:
                optionCodes = ""
                status['optionCodes'] = 'none'

            df = DataFrame(data_load.componentSerialNumber(str(data.get('native_pin', 0))))
            if df.shape[0] > 0:
                componentSerialNumber = dash_table_fetch(df)
                status['componentSerialNumber'] = 'block'
            else:
                componentSerialNumber = ""
                status['componentSerialNumber'] = 'none'

            df = DataFrame(data_load.factoryOptions(str(data.get('native_pin', 0))))
            if df.shape[0] > 0:
                factoryOptions = dash_table_fetch(df)
                status['factoryOptions'] = 'block'
            else:
                factoryOptions = ""
                status['factoryOptions'] = 'none'

            df = DataFrame(data_load.firmware_index(str(data.get('mach_id', 0))))
            if df.shape[0] > 0:
                firmware_df = dash_table_fetch_two_col(df)
                status['firmware_df'] = 'block'
            else:
                firmware_df = ""
                status['firmware_df'] = 'none'

            df = DataFrame(data_load.product_information(str(data.get('prod_id', 0))))
            if df.shape[0] > 0:
                prod_info = dash_table_fetch(df)
                status['prod_info'] = 'block'
            else:
                prod_info = ""
                status['prod_info'] = 'none'

            df = DataFrame(data_load.pin_info(str(data.get('mach_id', 0))))
            if df.shape[0] > 0:
                pin_info = dash_table_fetch(df)
                status['pin_info'] = 'block'
            else:
                pin_info = ""
                status['pin_info'] = 'none'

            df = DataFrame(data_load.dealer_info(str(data.get('mach_id', 0))))
            if df.shape[0] > 0:
                dealer = dash_table_fetch(df)
                status['dealer'] = 'block'
            else:
                dealer = ""
                status['dealer'] = 'none'

            df = DataFrame(data_load.jdcp_index(str(data.get('mach_id', 0))))
            if df.shape[0] > 0:

                jdcp = dash_table.DataTable(
                    id="table",
                    columns=[{"name": i, "id": i} for i in df.columns],
                    data=df.to_dict("records"),
                    style_data_conditional=[
                        {
                            'if': {
                                'column_id': 'Upgrade',
                            },
                            'font-weight': 'bold',
                            'color': 'red'
                        }],
                    style_header={
                        'text-align': 'center',
                        'backgroundColor': 'rgb(210, 210, 210)',
                        'color': 'green',
                        'fontWeight': 'bold'
                    },
                    style_cell={'font-size': '1.5vh', 'fontFamily': 'Arial', 'maxWidth': '250px', 'height': 'auto', 'maxHeight': '50px', 'padding': '5px'},
                    style_table={"height": "400px", "overflowX": "auto", "overflowY": "auto", "border": "none"},
                    style_data={'text-align': 'left', 'border': 'none', 'color': 'black', 'backgroundColor': 'white'}

                )
                status['jdcp'] = 'block'
            else:
                jdcp = ""
                status['jdcp'] = 'none'

            return measures, {'display': status['measures']}, warranty, {'display': status['warranty']}, warranty_claim, {'display': status['warranty_claim']}, DTAC_ccms,\
                   {'display': status['DTAC_ccms']}, elips_history, {'display': status['elips_history']}, pip_history, {'display': status['pip_history']}, \
                   optionCodes, {'display': status['optionCodes']}, componentSerialNumber, {'display': status['componentSerialNumber']}, factoryOptions, {'display': status['factoryOptions']}, \
                   firmware_df, {'display': status['firmware_df']}, prod_info, {'display': status['prod_info']}, pin_info, {'display': status['pin_info']}, \
                   dealer, {'display': status['dealer']}, jdcp, {'display': status['jdcp']}, ""
        except Exception as e:
            print("Exception :" + str(e))
            return "", {'display': 'none'}, "", {'display': 'none'}, "", {'display': 'none'}, "", {'display': 'none'}, "", {'display': 'none'}, "", {'display': 'none'}, "", {'display': 'none'}, "", {'display': 'none'}, "", {'display': 'none'}, "", {'display': 'none'}, "", {'display': 'none'}, "", {
                'display': 'none'}, "", {'display': 'none'}, "", {'display': 'none'}, ""

    else:
        return "", {'display': 'none'}, "", {'display': 'none'}, "", {'display': 'none'}, "", {'display': 'none'}, "", {'display': 'none'}, "", {'display': 'none'}, "", {'display': 'none'}, "", {'display': 'none'}, "", {'display': 'none'}, "", {'display': 'none'}, "", {'display': 'none'}, "", {
            'display': 'none'}, "", {'display': 'none'}, "", {'display': 'none'}, ""
