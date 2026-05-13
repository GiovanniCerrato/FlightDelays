import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self._choicePartenza = None
        self._choiceArrivo = None

    def handleAnalizza(self,e):
        cMinTxt = self._view._txtInCMin.value
        try:
            cMinTxt = int(cMinTxt)
        except ValueError:
            self._view._txtResults.clean()
            self._view._txtResults.controls.append(ft.Text(f"Inserire un valore numerico",color="red"))
            self._view.update_page()
            return
        if cMinTxt <= 0:
            self._view._txtResults.clean()
            self._view._txtResults.controls.append(ft.Text(f"Inserire un valore numerico maggiore di 0",color="red"))
            self._view.update_page()
            return

        self._model.buildGraph(cMinTxt)

        allNodes = self._model.getAllNodes()
        self._fillDropdown(allNodes)
        nNodes, nEdges = self._model.getGraphDetails()
        self._view._txtResults.clean()
        self._view._txtResults.controls.append(ft.Text(f"Grafo correttamente creato:", color="green"))
        self._view._txtResults.controls.append(ft.Text(f"Il grafo contiene {nNodes} nodi e {nEdges} archi", color="red"))
        self._view.update_page()
        return

    def _fillDropdown(self,allNodes):
        for n in allNodes:
            self._view._ddAeroportoP.options.append(
                ft.dropdown.Option(data= n,
                                   key = n.IATA_CODE,
                                   on_click = self._choiceDdPartenza)
            )
        for n in allNodes:
            self._view._ddAeroportoA.options.append(
                ft.dropdown.Option(data= n,
                                   key = n.IATA_CODE,
                                   on_click = self._choiceDdArrivo)
            )
    def _choiceDdPartenza(self,e):
        self._choicePartenza = e.control.data
        print(f"Hai selezionato come aeroporto di partenza {self._choicePartenza}")

    def _choiceDdArrivo(self,e):
        self._choiceArrivo = e.control.data
        print(f"Hai selezionato come aeroporto di arrivo {self._choiceArrivo}")

    def handleConnessi(self,e):
        pass

    def handleCerca(self,e):
        pass