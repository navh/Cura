from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot, pyqtProperty
from UM.Application import Application

import LayerView


class LayerViewProxy(QObject):
    def __init__(self, parent = None):
        super().__init__(parent)
        self._current_layer = 0
        self._controller = Application.getInstance().getController()
        self._controller.activeViewChanged.connect(self._onActiveViewChanged)
        self._onActiveViewChanged()
    
    currentLayerChanged = pyqtSignal()
    maxLayersChanged = pyqtSignal()
    activityChanged = pyqtSignal()

    @pyqtProperty(bool, notify = activityChanged)
    def getLayerActivity(self):
        active_view = self._controller.getActiveView()
        if type(active_view) == LayerView.LayerView.LayerView:
            return active_view.getActivity()

    @pyqtProperty(int, notify = maxLayersChanged)
    def numLayers(self):
        active_view = self._controller.getActiveView()
        if type(active_view) == LayerView.LayerView.LayerView:
            return active_view.getMaxLayers()
        #return 100
    
    @pyqtProperty(int, notify = currentLayerChanged)
    def currentLayer(self):
        active_view = self._controller.getActiveView()
        if type(active_view) == LayerView.LayerView.LayerView:
            return active_view.getCurrentLayer()

    @pyqtProperty(int, notify = currentLayerChanged)
    def minimumLayer(self):
        active_view = self._controller.getActiveView()
        if type(active_view) == LayerView.LayerView.LayerView:
            return active_view.getMinimumLayer()

    busyChanged = pyqtSignal()
    @pyqtProperty(bool, notify = busyChanged)
    def busy(self):
        active_view = self._controller.getActiveView()
        if type(active_view) == LayerView.LayerView.LayerView:
            return active_view.isBusy()

        return False

    @pyqtProperty(bool)
    def compatibilityMode(self):
        active_view = self._controller.getActiveView()
        if type(active_view) == LayerView.LayerView.LayerView:
            return active_view.getCompatibilityMode()

        return False

    @pyqtSlot(int)
    def setCurrentLayer(self, layer_num):
        active_view = self._controller.getActiveView()
        if type(active_view) == LayerView.LayerView.LayerView:
            active_view.setLayer(layer_num)

    @pyqtSlot(int)
    def setMinimumLayer(self, layer_num):
        active_view = self._controller.getActiveView()
        if type(active_view) == LayerView.LayerView.LayerView:
            active_view.setMinimumLayer(layer_num)

    @pyqtSlot(int)
    def setLayerViewType(self, layer_view_type):
        active_view = self._controller.getActiveView()
        if type(active_view) == LayerView.LayerView.LayerView:
            active_view.setLayerViewType(layer_view_type)

    @pyqtSlot(bool)
    def setOnlyColorActiveExtruder(self, only_color_active_extruder):
        active_view = self._controller.getActiveView()
        if type(active_view) == LayerView.LayerView.LayerView:
            active_view.setOnlyColorActiveExtruder(only_color_active_extruder)

    # Opacity 0..1
    @pyqtSlot(int, float)
    def setExtruderOpacity(self, extruder_nr, opacity):
        active_view = self._controller.getActiveView()
        if type(active_view) == LayerView.LayerView.LayerView:
            active_view.setExtruderOpacity(extruder_nr, opacity)

    @pyqtSlot(int)
    def setShowTravelMoves(self, show):
        active_view = self._controller.getActiveView()
        if type(active_view) == LayerView.LayerView.LayerView:
            active_view.setShowTravelMoves(show)

    @pyqtSlot(int)
    def setShowSupport(self, show):
        active_view = self._controller.getActiveView()
        if type(active_view) == LayerView.LayerView.LayerView:
            active_view.setShowSupport(show)

    @pyqtSlot(int)
    def setShowAdhesion(self, show):
        active_view = self._controller.getActiveView()
        if type(active_view) == LayerView.LayerView.LayerView:
            active_view.setShowAdhesion(show)

    @pyqtSlot(int)
    def setShowSkin(self, show):
        active_view = self._controller.getActiveView()
        if type(active_view) == LayerView.LayerView.LayerView:
            active_view.setShowSkin(show)

    @pyqtSlot(int)
    def setShowInfill(self, show):
        active_view = self._controller.getActiveView()
        if type(active_view) == LayerView.LayerView.LayerView:
            active_view.setShowInfill(show)

    def _layerActivityChanged(self):
        self.activityChanged.emit()
            
    def _onLayerChanged(self):
        self.currentLayerChanged.emit()
        self._layerActivityChanged()
        
    def _onMaxLayersChanged(self):
        self.maxLayersChanged.emit()

    def _onBusyChanged(self):
        self.busyChanged.emit()
        
    def _onActiveViewChanged(self):
        active_view = self._controller.getActiveView()
        if type(active_view) == LayerView.LayerView.LayerView:
            active_view.currentLayerNumChanged.connect(self._onLayerChanged)
            active_view.maxLayersChanged.connect(self._onMaxLayersChanged)
            active_view.busyChanged.connect(self._onBusyChanged)
